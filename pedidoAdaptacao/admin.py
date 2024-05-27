from django.contrib import admin
from django import forms
from pedidoAdaptacao.models import Etapa,PedidoAdaptacao, Avaliacao, Adaptacao, Diagramacao, Esteriotipia, Encadernacao, Revisao, Impressao, Transcricao
# Register your models here.


class EtapaAdmin(admin.ModelAdmin):
    pass

class EtapaInline(admin.StackedInline):
    model = Etapa
    extra = 1

class AdaptacaoInline(admin.StackedInline):
    model = Adaptacao
    extra = 0

class DiagramacaoInline(admin.StackedInline):
    model = Diagramacao
    extra = 0

class EsteriotipiaInline(admin.StackedInline):
    model = Esteriotipia
    extra = 0

class EncadernacaoInline(admin.StackedInline):
    model = Encadernacao
    extra = 0

class RevisaoInline(admin.StackedInline):
    model = Revisao
    extra = 0

class ImpressaoInline(admin.StackedInline):
    model = Impressao
    extra = 0

class TranscricaoInline(admin.StackedInline):
    model = Transcricao
    extra = 0

class PedidoAdaptacaoAdmin(admin.ModelAdmin):
    inlines = [TranscricaoInline, AdaptacaoInline, DiagramacaoInline, EsteriotipiaInline, EncadernacaoInline, ImpressaoInline]
    search_fields = ['solicitante']
    autocomplete_fields = ['solicitante','material']
 

admin.site.register(PedidoAdaptacao, PedidoAdaptacaoAdmin)
admin.site.register(Etapa, EtapaAdmin)
