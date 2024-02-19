from django.contrib import admin
from cliente.models import *


class AssinaturaAdmin(admin.ModelAdmin):
    raw_id_fields = ('material',)
    autocomplete_fields = ('material',) 
    exclude = ('data_ultima_alteracao',)

class ClienteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Assinatura, AssinaturaAdmin)
