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
    verbose_name_plural = 'Materiais'

class MaterialAdaptadoAdmin(admin.ModelAdmin):
    search_fields = ['material__titulo','tipo']

admin.site.register(Material, MaterialAdmin)
admin.site.register(MaterialAdaptado, MaterialAdaptadoAdmin)
