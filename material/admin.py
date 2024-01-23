from django.contrib import admin
from material.models import Material, MaterialAmpliado, MaterialBraille

# Register your models here.


class MaterialBrailleInline(admin.StackedInline):
    model = MaterialBraille
    can_delete = False 
    verbose_name_plural = 'Materiais Brailles'
    extra = 0

class MaterialAmpliadoInline(admin.StackedInline):
    model = MaterialAmpliado
    can_delete = False  
    verbose_name_plural = 'Materiais Ampliados'
    extra = 0

class MaterialAdmin(admin.ModelAdmin):
    inlines = [MaterialBrailleInline, MaterialAmpliadoInline]
    verbose_name_plural = 'Materiais Ampliados'

admin.site.register(Material, MaterialAdmin)
# 

