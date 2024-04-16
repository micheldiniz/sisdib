from django.contrib import admin
from cliente.models import *
from django.db.models import Q
from typing import Any
from django.contrib import admin
from django.db.models.fields.related import ForeignKey
from django.forms.models import ModelChoiceField
from django.http import HttpRequest
from django.db.models import Q

@admin.action(description='cancelar assinatura(s)')
def cancela_assinatura(modeladmin, request, queryset):
    queryset.update(estado='cancelado', observacao='Cancelamento realizado em lote')


class AssinanteInline(admin.StackedInline):
    model = Assinante    
    extra = 0

class AssinaturaAdmin(admin.ModelAdmin):
    inlines = [AssinanteInline]
    list_display = ['material','solicitante','data_registro', 'estado', 'observacao', 'data_ultima_alteracao']
    list_editable = ['estado', 'observacao']
    search_fields = ['material__material__titulo','estado','solicitante__pessoa__nome']
    # raw_id_fields = ('material', )
    # autocomplete_fields = ('material','solicitante')
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
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['pessoa__nome','pessoa__nacionalidade', 'pessoa__endereco__pais']    

class RegistroEnvioRevistasAdmin(admin.ModelAdmin):
    search_fields = ['revistas__material']
    list_display = ['descricao','data_envio','get_assinaturas','data_registro', 'observacao']
    autocomplete_fields = ['revistas']
    # formfield_overrides = {
    #     models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    # }
    def get_assinaturas(self, obj):
        return "\n".join([str(p) for p in obj.revistas.all()])
    get_assinaturas.short_description = 'Assinaturas enviadas'

admin.site.register(RegistroEnvioRevistas, RegistroEnvioRevistasAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Assinatura, AssinaturaAdmin)
