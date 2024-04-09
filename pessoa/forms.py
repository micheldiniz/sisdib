from django import forms
from .models import PessoaFisica, PessoaJuridica, Endereco, Contato
from cliente.models import Cliente

class PessoaFisicaRegistrationForm(forms.ModelForm):
    class Meta:
        model = PessoaFisica
        fields = ['nome', 'cpf', 'data_nascimento','is_estrangeiro']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }

class PessoaJuridicaRegistrationForm(forms.ModelForm):
    class Meta:
        model = PessoaJuridica
        fields = ['nome', 'cnpj']

class EnderecoRegistrationForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['cep', 'logradouro', 'numero', 'complemento', 'cidade', 'estado']

class ContatoRegistrationForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome_contato', 'email', 'telefone', 'celular']

class ClienteRegistrationForm(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = ['pessoa']