from django.contrib import admin
from django import forms
from pessoa.models import *
from pedido.models import Pedido
from django.utils.safestring import mark_safe

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
    list_display = ['nome', 'get_pedidos']
    inlines = [
        EnderecoInline,
        ContatoInline
    ]

    def get_pedidos(self, obj):
        pedidos = Pedido.objects.filter(solicitante__pessoa = obj)
        
        links = []
        for pedido in pedidos:
            link = '<li><a href="{0}">{1}</a></li>'.format(pedido.get_admin_url(), str(pedido))
            links.append(link)
        
        
        html_content = ''.join(links)
        html_content = '<ul>' + html_content + '</ul>'

        return mark_safe(html_content)

    get_pedidos.short_description = 'pedidos'

admin.site.register(PessoaJuridica, PessoaJuridicaAdmin)
admin.site.register(PessoaFisica, PessoaFisicaAdmin)
# admin.site.register(Pessoa, PessoaAdmin)
