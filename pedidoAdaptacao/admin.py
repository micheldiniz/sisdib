from django.contrib import admin
from pedidoAdaptacao.models import Etapa,PedidoAdaptacao
# Register your models here.

class PedidoAdaptacaoAdmin(admin.ModelAdmin):
    pass


admin.site.register(PedidoAdaptacao, PedidoAdaptacaoAdmin)
