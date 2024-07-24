from django.contrib import admin
from material.models import Material, MaterialAdaptado, Classificacao

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
    list_display = ['material_titulo','tipo','is_disponivel_para_pedido']
    list_editable = ['is_disponivel_para_pedido']
    autocomplete_fields = ('material',)

    def material_titulo(self, obj):
        return obj.material.titulo if obj.material else None

    material_titulo.short_description = 'Título do material'

class ClassificacaoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Classificacao, ClassificacaoAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(MaterialAdaptado, MaterialAdaptadoAdmin)
