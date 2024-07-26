from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from material.models import Material, MaterialAdaptado, Classificacao
from pedido.models import ItemPedido
from django.db.models import Count

# Register your models here.

class MaterialAdaptadoInline(admin.StackedInline):
    model = MaterialAdaptado
    can_delete = True  
    verbose_name_plural = 'Materiais Adaptados'
    extra = 0

class MaterialAdmin(admin.ModelAdmin):
    inlines = [MaterialAdaptadoInline]
    search_fields = ['titulo','classificacao__classificacao','autor']


class MaterialAdaptadoAdmin(admin.ModelAdmin):   
    search_fields = ['material__titulo','tipo','material__autor']
    list_display = ['material_titulo','tipo','is_disponivel_para_pedido','item_pedido_count']
    list_editable = ['is_disponivel_para_pedido']
    autocomplete_fields = ('material',)

    def item_pedido_count(self, obj):
        items = obj.itempedido_set.all()
        total = 0
        for item in items:
            total += item.quantidade
        return total

    def material_titulo(self, obj):
        return obj.material.titulo if obj.material else None
    material_titulo.short_description = 'Título do material'

   

class ClassificacaoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Classificacao, ClassificacaoAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(MaterialAdaptado, MaterialAdaptadoAdmin)
