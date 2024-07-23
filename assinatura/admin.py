from django.contrib import admin
from assinatura.models import Solicitante,Assinatura,Assinante,RegistroEnvioAssinaturas,EdicaoRevistaAssinatura, Remessa, Revista, TipoRemessa
from pessoa.models import Endereco
from django.db.models import Q
from typing import Any
from django.contrib import admin
from django.db.models.fields.related import ForeignKey
from django.forms.models import ModelChoiceField
from django.http import HttpRequest, HttpResponse
from django.db.models import Q
from datetime import datetime
from django.utils.safestring import mark_safe
from django.shortcuts import render
from typing import List
from weasyprint import HTML

@admin.action(description='cancelar assinatura(s)')
def cancela_assinatura(modeladmin, request, queryset):
    queryset.update(estado='cancelado', observacao='Cancelamento realizado em lote', data_ultima_alteracao = datetime.now())

@admin.action(description='guia de correios')
def guia_correio(modeladmin, request, queryset):
    dict = {}
        
    for p in queryset:
        revistas  = []
        edicoes = get_edicoes(p)
        peso = 0
        pacotes = 0
        for e in edicoes:
            revistas.append(str(e.revista.titulo))
            peso += e.peso
            pacotes += e.assinaturas.count()
        remessas_qs = get_remessas(p)
        remessas = {}
        for remessa in remessas_qs:
            remessas[remessa.id] = remessa

        dict = {  'remessas' : remessas,
                  'remetente': p.remetente,
                  'identificacao': p.identificacao,
                  'classificacao': ' + '.join(revistas),
                  'peso': peso,
                  'pacotes':pacotes//2,
                }

    html_string = render(request, 'guia_correios_assinaturas.html', {'registroSaidaAssinaturas': dict }).content.decode('utf-8')

    pdf = HTML(string=html_string).write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="{0}.pdf"'.format('arquivo')

    return response
    # return render(request, 'guia_correios_assinaturas.html', {'registroSaidaAssinaturas': dict })


# def get_quantidade_pacotes(ra: RegistroEnvioAssinaturas):
#     edicoes = get_edicoes(ra)


@admin.action(description='gerar etiquetas')
def gerar_etiquetas(modeladmin, request, queryset):
    dict = {}
    
    for p in queryset:        
        edicoes = get_edicoes(p)   
        solicitantes = []
        for edicao in edicoes:
            [solicitantes.append(assinatura.solicitante) for assinatura in edicao.assinaturas.all()]            
        dict[p] = { 'solicitantes' : dict.fromkeys(solicitantes) }

    return render(request, 'etiquetas_assinaturas.html', {
        'registroSaidaAssinaturas': dict,
    })

def get_assinaturas(elem):    
    assinaturas = []
    for el in elem:
        assinaturas = el.assinaturas.all()
    return [assinatura for assinatura in assinaturas] 

def get_edicoes(ra: RegistroEnvioAssinaturas) -> List['EdicaoRevistaAssinatura']:
    edicoes_qs = EdicaoRevistaAssinatura.objects.filter(registro_envio = ra)
    return [edicoes for edicoes in edicoes_qs]

def get_remessas(ra: RegistroEnvioAssinaturas) -> List['Remessa']:
    remessas_qs = Remessa.objects.filter(registro_envio = ra)
    return [remessas for remessas in remessas_qs]

def atualizar_assinaturas_no_registro_de_saida(modeladmin, request, queryset):
    for p in queryset:        
        edicoes = get_edicoes(p)
        if p.enviado == False:
            for edicao in edicoes:            
                assinaturas = Assinatura.objects.filter(estado='vigente', revista=edicao.revista)            
                edicao.quantidade_assinaturas_Es = quantidade_assinaturas_es(assinaturas)
                edicao.quantidade_assinaturas_OE = quantidade_assinaturas_oe(assinaturas)
                edicao.quantidade_assinaturas_RJ = quantidade_assinaturas_rj(assinaturas)
                
                print(edicao.quantidade_assinaturas_Es)
                print(edicao.quantidade_assinaturas_OE)
                print(edicao.quantidade_assinaturas_RJ)


                edicao.assinaturas.set(assinaturas)
                edicao.save()             

def quantidade_assinaturas_es(ass):
    total = 0
    for a in ass:
        if(a.solicitante.pessoa.is_estrangeiro == True):
            # print(a.solicitante.pessoa)
            total += 1
    return total

def quantidade_assinaturas_oe(ass):
    total = 0
    for a in ass:
        if(get_UF_pessoa(a.solicitante) != 'RJ' and a.solicitante.pessoa.is_estrangeiro == False):
            print(a.solicitante.pessoa)
            total += 1
    return total

def quantidade_assinaturas_rj(ass):
    total = 0
    for a in ass:
        if(get_UF_pessoa(a.solicitante) == 'RJ' and a.solicitante.pessoa.is_estrangeiro == False):
            print(a.solicitante.pessoa)
            total += 1

    return total

def get_UF_pessoa(solicitante:Solicitante):    
    endereco = Endereco.objects.get(pessoa=solicitante.pessoa)
    return endereco.estado

class AssinanteInline(admin.StackedInline):
    model = Assinante    
    extra = 0

class AssinaturaAdmin(admin.ModelAdmin):
    # inlines = [AssinanteInline]
    list_display = ['revista','solicitante','data_registro', 'estado', 'observacao', 'data_ultima_alteracao']
    list_editable = ['estado', 'observacao']
    search_fields = ['revista_titulo','estado','solicitante__pessoa__nome']    
    autocomplete_fields = ['solicitante']
    exclude = ('data_ultima_alteracao',)
    actions = [cancela_assinatura]

    def formfield_for_foreignkey(self, db_field: ForeignKey[Any], request: HttpRequest | None, **kwargs: Any) -> ModelChoiceField | None:

        if db_field.name == 'revista':
            qs = super().formfield_for_foreignkey(db_field, request, **kwargs).queryset
            object_id = request.resolver_match.kwargs.get('object_id')
            
            if (object_id):
                assinatura_instance = Assinatura.objects.get(id=object_id)
                current_revista = assinatura_instance.revista
                filtered_qs = qs.filter(Q(is_disponivel_para_assinatura=True) | Q(revista = current_revista)).distinct()
                kwargs['queryset'] = filtered_qs

                return super().formfield_for_foreignkey(db_field, request, **kwargs)

            filtered_qs = qs.filter(Q(is_disponivel_para_assinatura=True)).distinct()
            kwargs['queryset'] = filtered_qs
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class SolicitanteAdmin(admin.ModelAdmin):
    search_fields = ['pessoa__nome','pessoa__nacionalidade', 'pessoa__endereco__pais']
    list_display = ['pessoa', 'assinaturas_ativas', 'assinaturas_canceladas']

    def assinaturas_ativas(self, obj):
        assinaturas = Assinatura.objects.filter(solicitante=obj, estado='vigente')
        if assinaturas.count() < 1:
            return 'nenhuma'
        assinaturas_html = []
        for assinatura in assinaturas:
            html = '<a href="{0}">{1}</a></br>'.format(assinatura.get_admin_url(),str(assinatura.revista))
            assinaturas_html.append(html)
        html_content = ''.join(assinaturas_html)
        return mark_safe(html_content)

    def assinaturas_canceladas(self, obj):
        assinaturas = Assinatura.objects.filter(solicitante=obj, estado='cancelado')
        if assinaturas.count() < 1:
            return 'nenhuma'
        assinaturas_html = []
        for assinatura in assinaturas:
            html = '<a href="{0}">{1}</a></br>'.format(assinatura.get_admin_url(),str(assinatura.revista))
            assinaturas_html.append(html)
        html_content = ''.join(assinaturas_html)
        return mark_safe(html_content)

class EdicaoRevistaAssinaturaInline(admin.StackedInline):    
    model = EdicaoRevistaAssinatura
    extra = 0
    readonly_fields = ['quantidade_assinaturas_RJ', 'quantidade_assinaturas_Es', 'quantidade_assinaturas_OE']
    exclude = ['assinaturas']

class RemessaInline(admin.StackedInline):
    model = Remessa
    extra = 0
    exclude = ['observacao','ordem']

class TipoRemessaAdmin(admin.ModelAdmin):
    model = TipoRemessa

class RegistroEnvioAssinaturasAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'assinaturas']
    list_display = ['nome','enviado','data_registro', 'observacao','get_quantidade_assinaturas','get_quantidade_paginas']        
    inlines = [EdicaoRevistaAssinaturaInline, RemessaInline]
    actions = [gerar_etiquetas, guia_correio, atualizar_assinaturas_no_registro_de_saida]

    # def save_related(self, request: Any, form: Any, formsets: Any, change: Any) -> None:
    #     super().save_related(request, form, formsets, change)
    
    def get_quantidade_assinaturas(self,obj):
        edicoes_relacionadas = EdicaoRevistaAssinatura.objects.filter(registro_envio = obj)
        total = 0
        for edicao in edicoes_relacionadas:
            total += edicao.assinaturas.count()
        return total

    def get_quantidade_paginas(self,obj):
        edicoes_relacionadas = EdicaoRevistaAssinatura.objects.filter(registro_envio = obj)        
        total_paginas = 0
        for edicao in edicoes_relacionadas:
            qtd_paginas = edicao.quantidade_paginas * edicao.assinaturas.count()
            total_paginas += qtd_paginas
        return total_paginas

    def get_assinaturas(self, obj):
        return "\n".join([str(p) for p in obj.assinaturas.all()])
    
    def get_total_assinaturas(self, obj):
        return obj.assinaturas.count()

    get_assinaturas.short_description = 'Assinaturas enviadas'
    get_total_assinaturas.short_description = 'Total de assinaturas enviadas'
    get_quantidade_assinaturas.short_description = 'Total assinaturas'
    get_quantidade_paginas.short_description = 'total paginas'

class RevistaAdmin(admin.ModelAdmin):
    pass



admin.site.register(Revista, RevistaAdmin)
admin.site.register(Solicitante, SolicitanteAdmin)
admin.site.register(Assinatura, AssinaturaAdmin)
admin.site.register(RegistroEnvioAssinaturas, RegistroEnvioAssinaturasAdmin)
admin.site.register(TipoRemessa, TipoRemessaAdmin)