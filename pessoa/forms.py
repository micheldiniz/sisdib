from django import forms
from .models import PessoaFisica, PessoaJuridica, Endereco, Contato
from cliente.models import Cliente

class PessoaFisicaRegistrationForm(forms.ModelForm):
    class Meta:
        model = PessoaFisica
        fields = ['nome', 'cpf', 'data_nascimento']
    # widgets = {
    #     'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
    # }        
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
        
    # You can customize the form widget or add validation if needed

    # def clean(self):
    #     cleaned_data = super().clean()
    #     pessoa_tipo = cleaned_data.get('pessoa_tipo')
    #     if pessoa_tipo == 'fisica':
    #     # Validate fields specific to PessoaFisica
    #     elif pessoa_tipo == 'juridica':
    #     # Validate fields specific to PessoaJuridica
    #     return cleaned_data
