from django.contrib import admin
from cliente.models import *

class AssinanteInline(admin.StackedInline):
    model = Assinante    
    extra = 0

class AssinaturaAdmin(admin.ModelAdmin):
    inlines = [AssinanteInline]
    list_display = ['material','solicitante','data_registro', 'estado', 'observacao', 'data_ultima_alteracao']
    list_editable = ['estado', 'observacao']
    raw_id_fields = ('material', )
    autocomplete_fields = ('material','solicitante') 
    exclude = ('data_ultima_alteracao',)


class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['pessoa__nome','pessoa__nacionalidade', 'pessoa__endereco__pais']

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Assinatura, AssinaturaAdmin)
