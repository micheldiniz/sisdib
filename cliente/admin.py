from django.contrib import admin
from django.db.models.fields.reverse_related import ForeignObjectRel
from cliente.models import Solicitante,Assinatura,Assinante,RegistroEnvioAssinaturas,EdicaoMaterialAssinatura, Remessa
from django.db.models import Q
from typing import Any
from django.contrib import admin
from django.db.models.fields.related import ForeignKey
from django.forms.models import ModelChoiceField
from django.http import HttpRequest
from django.db.models import Q
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from datetime import datetime
from django.utils.safestring import mark_safe
from django.shortcuts import render
from typing import List

@admin.action(description='cancelar assinatura(s)')
def cancela_assinatura(modeladmin, request, queryset):
    queryset.update(estado='cancelado', observacao='Cancelamento realizado em lote', data_ultima_alteracao = datetime.now())

@admin.action(description='guia de correios')
def guia_correio(modeladmin, request, queryset):
    dict = {}
        
    for p in queryset:
        materiais_adaptados  = []
        edicoes = get_edicoes(p)
        peso = 0
        pacotes = 0
        for e in edicoes:
            materiais_adaptados.append(str(e.material.material.titulo))
            peso += e.peso
            pacotes += e.assinaturas.count()
        remessas_qs = get_remessas(p)
        remessas = {}
        for remessa in remessas_qs:
            remessas[remessa.id] = remessa

        dict = {  'remessas' : remessas,
                  'remetente': p.remetente,
                  'identificacao': p.identificacao,
                  'classificacao': ' + '.join(materiais_adaptados),
                  'peso': peso,
                  'pacotes':pacotes//2,
                }

    return render(request, 'guia_correios_assinaturas.html', {
        'registroSaidaAssinaturas': dict,
    })

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

def get_edicoes(ra: RegistroEnvioAssinaturas) -> List['EdicaoMaterialAssinatura']:
    edicoes_qs = EdicaoMaterialAssinatura.objects.filter(registro_envio = ra)
    return [edicoes for edicoes in edicoes_qs]

def get_remessas(ra: RegistroEnvioAssinaturas) -> List['Remessa']:
    remessas_qs = Remessa.objects.filter(registro_envio = ra)
    return [remessas for remessas in remessas_qs]

def atualizar_assinaturas_no_registro_de_saida(modeladmin, request, queryset):
    for p in queryset:        
        edicoes = get_edicoes(p)   
        if p.enviado == False:
            for edicao in edicoes:            
                assinaturas = Assinatura.objects.filter(estado='vigente', material=edicao.material)            
                edicao.assinaturas.set(assinaturas)

def atualizar_remessas(modeladmin, request, queryset):
    # for p in queryset:
    #      assinaturas = []
    #      edicoes = get_edicoes(p)
    #      for e in edicoes:
    #         assinaturas = e.assinaturas
    #         assinaturas.filter(pessoa='')
    pass
        

class AssinanteInline(admin.StackedInline):
    model = Assinante    
    extra = 0

class AssinaturaAdmin(admin.ModelAdmin):
    # inlines = [AssinanteInline]
    list_display = ['material','solicitante','data_registro', 'estado', 'observacao', 'data_ultima_alteracao']
    list_editable = ['estado', 'observacao']
    search_fields = ['material__material__titulo','estado','solicitante__pessoa__nome', 'material__tipo']    
    autocomplete_fields = ['solicitante']
    exclude = ('data_ultima_alteracao',)
    actions = [cancela_assinatura]

    def formfield_for_foreignkey(self, db_field: ForeignKey[Any], request: HttpRequest | None, **kwargs: Any) -> ModelChoiceField | None:

        if db_field.name == 'material':
            qs = super().formfield_for_foreignkey(db_field, request, **kwargs).queryset
            object_id = request.resolver_match.kwargs.get('object_id')
            
            if (object_id):
                assinatura_instance = Assinatura.objects.get(id=object_id)
                current_material = assinatura_instance.material
                filtered_qs = qs.filter(Q(is_disponivel_para_assinatura=True) | Q(material__materialadaptado = current_material)).distinct()
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
            html = '<a href="{0}">{1}</a></br>'.format(assinatura.get_admin_url(),str(assinatura.material))
            assinaturas_html.append(html)
        html_content = ''.join(assinaturas_html)
        return mark_safe(html_content)

    def assinaturas_canceladas(self, obj):
        assinaturas = Assinatura.objects.filter(solicitante=obj, estado='cancelado')
        if assinaturas.count() < 1:
            return 'nenhuma'
        assinaturas_html = []
        for assinatura in assinaturas:
            html = '<a href="{0}">{1}</a></br>'.format(assinatura.get_admin_url(),str(assinatura.material))
            assinaturas_html.append(html)
        html_content = ''.join(assinaturas_html)
        return mark_safe(html_content)

class EdicaoMaterialAssinaturaInline(admin.StackedInline):    
    model = EdicaoMaterialAssinatura
    extra = 0
    # readonly_fields = ['assinaturas']
    exclude = ['assinaturas']

class RemessaInline(admin.StackedInline):
    model = Remessa
    extra = 0
    readonly_fields = ['quantidade']
    exclude = ['observacao','ordem']

class RegistroEnvioAssinaturasAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'assinaturas']
    list_display = ['nome','enviado','data_registro', 'observacao','get_quantidade_assinaturas','get_quantidade_paginas']        
    inlines = [EdicaoMaterialAssinaturaInline, RemessaInline]
    actions = [gerar_etiquetas, guia_correio, atualizar_assinaturas_no_registro_de_saida]

    # def save_related(self, request: Any, form: Any, formsets: Any, change: Any) -> None:
    #     super().save_related(request, form, formsets, change)
    
    def get_quantidade_assinaturas(self,obj):
        edicoes_relacionadas = EdicaoMaterialAssinatura.objects.filter(registro_envio = obj)
        total = 0
        for edicao in edicoes_relacionadas:
            total += edicao.assinaturas.count()
        return total

    def get_quantidade_paginas(self,obj):
        edicoes_relacionadas = EdicaoMaterialAssinatura.objects.filter(registro_envio = obj)        
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


admin.site.register(Solicitante, SolicitanteAdmin)
admin.site.register(Assinatura, AssinaturaAdmin)
admin.site.register(RegistroEnvioAssinaturas, RegistroEnvioAssinaturasAdmin)