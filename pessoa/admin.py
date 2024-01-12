from django.contrib import admin
from pessoa.models import *
# Register your models here.
class PessoaFisicaAdmin(admin.ModelAdmin):
    pass

class PessoaJuridicaAdmin(admin.ModelAdmin):
    pass

class EnderecoInline(admin.TabularInline):
    model = Endereco

class ContatoInline(admin.TabularInline):
    model = Contato

class PessoaAdmin(admin.ModelAdmin):
    inlines = [
        EnderecoInline,
        ContatoInline,
    ]


admin.site.register(PessoaJuridica, PessoaJuridicaAdmin)
admin.site.register(PessoaFisica, PessoaFisicaAdmin)
admin.site.register(Pessoa, PessoaAdmin)
