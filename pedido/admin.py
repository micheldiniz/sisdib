from django.contrib import admin
from pedido.models import Pedido, Item

# Register your models here.

class PedidoAdmin(admin.ModelAdmin):
    pass

class ItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Item, ItemAdmin)