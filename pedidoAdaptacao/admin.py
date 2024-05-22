from django.contrib import admin
from pedidoAdaptacao.models import Etapa,PedidoAdaptacao
# Register your models here.


class EtapaAdmin(admin.ModelAdmin):
    pass

class EtapaInline(admin.StackedInline):
    model = Etapa
    extra = 1


class PedidoAdaptacaoAdmin(admin.ModelAdmin):
    inlines = [EtapaInline]


admin.site.register(PedidoAdaptacao, PedidoAdaptacaoAdmin)
admin.site.register(Etapa, EtapaAdmin)
