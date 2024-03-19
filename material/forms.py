from django import forms
from material.models import MaterialAdaptado, Material
from django.forms.models import inlineformset_factory

# class MaterialForm(forms.ModelForm):
    # class Meta:
    #     model = Material
    #     fields = ['titulo', 'classificacao', 'acervo', 'tiragem', 'quantidade_paginas']

class MaterialAdaptadoForm(forms.ModelForm):
    class Meta:
        model = MaterialAdaptado
        fields = ['material', 'tipo', 'quantidade_paginas', 'partes', 'is_disponivel_para_assinatura','is_disponivel_para_pedido','arquivo']
        labels = {
            'material':'Material',
            'tipo':'Tipo',
            'quantidade_paginas':'Quantidade de Páginas',
            'partes':'Partes',
            'is_disponivel_para_assinatura': 'Disponível para Assinatura',
            'is_disponivel_para_pedido':'Disponível para Pedido',
            'arquivo':'Arquivo',
        }
#         widgets = {
#             'material': forms.Select(attrs={'class':'form-control'}),
#             'tipo': forms.Select(attrs={'class': 'form-control'}),
#             'quantidade_paginas': forms.NumberInput(attrs={'class':'from-control'}),
#             'partes': forms.NumberInput(attrs={'class':'from-control'}),
#             'is_disponivel_para_assinatura': forms.CheckboxInput(attrs={'class':'from-control'}),
#             'is_disponivel_para_pedido': forms.CheckboxInput(attrs={'class':'from-control'}),
#             'arquivo': forms.FileInput(attrs={'class':'form-control-file'}),
#         }
#     def __init(self, *args,**kwargs):
#         super(MaterialAdaptadoForm, self).__init__(*args, **kwargs)
#         self.material_formset = MaterialAdaptadoFormSet(instance=self.instance)

#     def is_valid(self):
#         return super(MaterialAdaptadoForm, self).is_valid() and self.material_formset.is_valid()

#     def save(self, commit = True):
#         instance = super(MaterialAdaptadoForm, self).save(commit=commit)
#         self.material_formset.instance = instance
#         self.material_formset.save(commit=commit)
#         return instance

# MaterialAdaptadoFormSet = inlineformset_factory(Material, MaterialAdaptado, form=MaterialAdaptadoForm, extra=1, can_delete=True)