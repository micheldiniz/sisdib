from django.contrib import admin
from django.db.models.fields.reverse_related import ForeignObjectRel
from cliente.models import Solicitante,Assinatura,Assinante,RegistroEnvioAssinaturas,EdicaoMaterialAssinatura
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

@admin.action(description='cancelar assinatura(s)')
def cancela_assinatura(modeladmin, request, queryset):
    queryset.update(estado='cancelado', observacao='Cancelamento realizado em lote', data_ultima_alteracao = datetime.now())


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
    readonly_fields = ['assinaturas']

class RegistroEnvioAssinaturasAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'assinaturas']
    list_display = ['nome','data_envio','data_registro', 'observacao']        
    inlines = [EdicaoMaterialAssinaturaInline]

    # def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
    #     super().save_model(request, obj, form, change)    
    #     print(form)
    #     for inline_obj in form.cleaned_data['edicaomaterialassinatura_set']:
    #         print(inline_obj)
    #     # return super().save_model(request, obj, form, change)    

    def save_related(self, request: Any, form: Any, formsets: Any, change: Any) -> None:
        super().save_related(request, form, formsets, change)
        print('################################################')
        print(formsets)
        print(form)
        print(change)





    def get_assinaturas(self, obj):
        return "\n".join([str(p) for p in obj.assinaturas.all()])
    
    def get_total_assinaturas(self, obj):
        return obj.assinaturas.count()

    get_assinaturas.short_description = 'Assinaturas enviadas'
    get_total_assinaturas.short_description = 'Total de assinaturas enviadas'

admin.site.register(Solicitante, SolicitanteAdmin)
admin.site.register(Assinatura, AssinaturaAdmin)
admin.site.register(RegistroEnvioAssinaturas, RegistroEnvioAssinaturasAdmin)