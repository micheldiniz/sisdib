from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import RegistroEnvioPedidos, Pedido

class RegistroEnvioPedidosForm(forms.ModelForm):
    pedidos = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,required=False)
    
    class Meta:
        model = RegistroEnvioPedidos
        fields = ['descricao','data_envio','observacao','pedidos']
        widgets = {
            'data_envio': forms.DateInput(attrs={'type':'date'})
        }

    def __init__(self,data: Mapping[str, Any] | None = ..., files: Mapping[str, File] | None = ..., auto_id: bool | str = ..., prefix: str | None = ..., initial: dict[str, Any] | None = ..., error_class: ErrorList = ..., label_suffix: str | None = ..., empty_permitted: bool = ..., instance: Model | None = ..., use_required_attribute: bool | None = ..., renderer: Any = ...) -> None:
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance, use_required_attribute, renderer)
        self.fields['pedidos'].queryset = Pedido.objects.filter(estado_do_pedido='novo')

class PedidoForm(forms.ModelForm):
    pass

