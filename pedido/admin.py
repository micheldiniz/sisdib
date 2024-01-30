from django.contrib import admin
from pedido.models import Pedido, ItemPedido

# Register your models here.

class PedidoAdmin(admin.ModelAdmin):
    pass

class ItemPedidoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Pedido, PedidoAdmin)
admin.site.register(ItemPedido, ItemPedidoAdmin)