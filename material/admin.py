from django.contrib import admin
from django import forms
from material.models import Material, MaterialAdaptado

# Register your models here.


class MaterialAdaptadoForm(forms.ModelForm):
    class Meta:
        model = MaterialAdaptado
        fields = '__all__'

    def clean_foreign_key_field(self):
        foreign_key_value = self.cleaned_data.get('material')

        count = MaterialAdaptado.objects.filter(material=foreign_key_value).count()

        if count > 2:
            raise forms.ValidateError("não é permitido mais de 2 itens relacionados à um material")
        return foreign_key_value

class MaterialAdaptadoInline(admin.StackedInline):
    model = MaterialAdaptado
    can_delete = True  
    verbose_name_plural = 'Materiais Adaptados'
    extra = 0

class MaterialAdmin(admin.ModelAdmin):
    inlines = [MaterialAdaptadoInline]
    verbose_name_plural = 'Materiais'

class MaterialAdaptadoAdmin(admin.ModelAdmin):
    # form = MaterialAdaptadoForm
    pass

admin.site.register(Material, MaterialAdmin)
admin.site.register(MaterialAdaptado, MaterialAdaptadoAdmin)
