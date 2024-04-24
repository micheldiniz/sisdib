from django.contrib import admin
from django import forms
from pessoa.models import *
# Register your models here.

class EnderecoInline(admin.StackedInline):
    model = Endereco
    extra = 1

class ContatoInline(admin.StackedInline):
    model = Contato
    extra = 1


class PessoaFisicaAdminForm(forms.ModelForm):
    class Meta:
        model = PessoaFisica
        fields = '__all__'

    # is_estrageiro_field = forms.BooleanField(
    #     widget = forms.RadioSelect(choices=[(True, "Sim"),(False, "Não")]),required=True,
    # )

class PessoaFisicaAdmin(admin.ModelAdmin):
    verbose_name_plural = "Pessoas Físicas"
    form = PessoaFisicaAdminForm
    search_fields = ['nome','is_estrangeiro']
    inlines = [
        EnderecoInline,
        ContatoInline
    ]


class PessoaJuridicaAdmin(admin.ModelAdmin):
    verbose_name_plural = "Pessoas Jurídicas"
    inlines = [
        EnderecoInline,
        ContatoInline
    ]


admin.site.register(PessoaJuridica, PessoaJuridicaAdmin)
admin.site.register(PessoaFisica, PessoaFisicaAdmin)
# admin.site.register(Pessoa, PessoaAdmin)
