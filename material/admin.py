from django.contrib import admin
from django import forms
from material.models import Material, MaterialAdaptado

# Register your models here.

class MaterialAdaptadoInline(admin.StackedInline):
    model = MaterialAdaptado
    can_delete = True  
    verbose_name_plural = 'Materiais Adaptados'
    extra = 0

class MaterialAdmin(admin.ModelAdmin):
    inlines = [MaterialAdaptadoInline]
    search_fields = ['titulo','classificacao']


class MaterialAdaptadoAdmin(admin.ModelAdmin):   
    search_fields = ['material__titulo','tipo']
    list_display = ['material_titulo','tipo','is_disponivel_para_pedido','is_disponivel_para_assinatura']
    list_editable = ['is_disponivel_para_pedido','is_disponivel_para_assinatura']
    autocomplete_fields = ('material',)

    def material_titulo(self, obj):
        return obj.material.titulo if obj.material else None

    material_titulo.short_description = 'Título do material'

admin.site.register(Material, MaterialAdmin)
admin.site.register(MaterialAdaptado, MaterialAdaptadoAdmin)
