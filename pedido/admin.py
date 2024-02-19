from django.contrib import admin
from pedido.models import Pedido, ItemPedido

# Register your models here.

class ItemPedidoInline(admin.StackedInline):
    model = ItemPedido
    extra = 1
    raw_id_fields = ('material',)
    autocomplete_fields = ('material',)
class PedidoAdmin(admin.ModelAdmin):
    inlines = [ItemPedidoInline]

admin.site.register(Pedido, PedidoAdmin)