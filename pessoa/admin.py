from django.contrib import admin
from pessoa.models import *
# Register your models here.

class EnderecoInline(admin.StackedInline):
    model = Endereco
    extra = 1

class ContatoInline(admin.StackedInline):
    model = Contato
    extra = 1

class PessoaFisicaAdmin(admin.ModelAdmin):
    verbose_name_plural = "Pessoas Físicas"
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
