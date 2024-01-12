from django.contrib import admin
from cliente.models import *


class AssinaturaAdmin(admin.ModelAdmin):
    pass

class ClienteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Assinatura, AssinaturaAdmin)
