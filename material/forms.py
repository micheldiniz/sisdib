from django import forms
from material.models import MaterialAdaptado, Material
from django.forms.models import inlineformset_factory

class YesNoBooleanField(forms.BooleanField):
    def __init__(self, *args, **kwargs):
        initial = kwargs.pop('initial', False)  # Default to True (Yes)
        super().__init__(*args, **kwargs)
        self.initial = initial

    widget = forms.RadioSelect(choices=((True, 'Sim'), (False, 'Não')))


class MaterialForm(forms.ModelForm):
    titulo = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    autor = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    edicao = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    editora = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    publico_alvo = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    acervo = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    tiragem = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )    
    
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
            'quantidade_paginas': forms.TextInput(attrs={'class': 'form-control'}),
            'classificacao': forms.Select(attrs={'class': 'form-select'}),
        }
        

class MaterialAdaptadoForm(forms.ModelForm):

    is_disponivel_para_pedido = YesNoBooleanField(        
        label='Disponível para Pedido?'        
    )

    class Meta:
        model = MaterialAdaptado
        fields = ['material','tipo', 'quantidade_paginas', 'partes', 'tamanho','is_disponivel_para_pedido','arquivo']        
        labels = {
            'material':'Material',
            'tipo':'Tipo',
            'quantidade_paginas':'Quantidade de Páginas',
            'tamanho':'Tamanho (Mb ou Kg)',
            'partes':'Partes',
            'is_disponivel_para_pedido':'Disponível para Pedido?',
            'arquivo':'Arquivo adaptado',
        }
        widgets = {
            'material': forms.Select(attrs={'class':'form-select'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'quantidade_paginas': forms.TextInput(attrs={'class': 'form-control'}),
            'partes': forms.TextInput(attrs={'class': 'form-control'}),
            'tamanho': forms.TextInput(attrs={'class': 'form-control'}),
            'is_disponivel_para_pedido': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'arquivo': forms.FileInput(attrs={'class': 'form-control'}),
            # 'material': Select2Widget,
        }


MaterialAdaptadoFormSet = inlineformset_factory(Material, MaterialAdaptado, form=MaterialAdaptadoForm, extra=1, can_delete=True)