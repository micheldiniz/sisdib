from django import forms
from material.models import MaterialAdaptado, Material
from django.forms.models import inlineformset_factory


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['classificacao','titulo','autor','edicao','editora','publico_alvo','acervo','tiragem','quantidade_paginas','arquivo_original',]
        labels = {
            'classificacao':'Classificação',
            'titulo':'Título',
            'autor':'Autor',
            'edicao':'Edição',
            'editora':'Editora',
            'publico_alvo':'Público alvo',
            'acervo':'Acervo',
            'tiragem':'Tiragem',
            'quantidade_paginas':'Quantidade de páginas',
            'arquivo_original':'Arquivo original',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        

class MaterialAdaptadoForm(forms.ModelForm):
    class Meta:
        model = MaterialAdaptado
        fields = ['tipo', 'quantidade_paginas', 'partes','tamanho','is_disponivel_para_pedido','arquivo']
        labels = {          
            'tipo':'Tipo',            
            'quantidade_paginas':'Quantidade de Páginas',
            'tamanho':'Tamanho',  
            'partes':'Partes',            
            'is_disponivel_para_pedido':'Disponível para Pedido',
            'arquivo':'Arquivo adaptado',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init(self, *args,**kwargs):
        super(MaterialAdaptadoForm, self).__init__(*args, **kwargs)
        self.material_formset = MaterialAdaptadoFormSet(instance=self.instance)

    def is_valid(self):
        return super(MaterialAdaptadoForm, self).is_valid() and self.material_formset.is_valid()

    def save(self, commit = True):
        instance = super(MaterialAdaptadoForm, self).save(commit=commit)
        self.material_formset.instance = instance
        self.material_formset.save(commit=commit)
        return instance

MaterialAdaptadoFormSet = inlineformset_factory(Material, MaterialAdaptado, form=MaterialAdaptadoForm, extra=1, can_delete=True)