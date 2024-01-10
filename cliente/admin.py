from django.contrib import admin
from cliente.models import *




class AssinaturaAdmin(admin.ModelAdmin):
    pass

class PessoaFisicaAdmin(admin.ModelAdmin):
    pass

class PessoaJuridicaAdmin(admin.ModelAdmin):
    pass

class EnderecoAdmin(admin.ModelAdmin):
    pass

class ContatoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contato, ContatoAdmin)
admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(PessoaJuridica, PessoaJuridicaAdmin)
admin.site.register(PessoaFisica, PessoaFisicaAdmin)
admin.site.register(Assinatura, AssinaturaAdmin)

