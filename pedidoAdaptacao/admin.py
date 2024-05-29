from django.contrib import admin
from django import forms
from pedidoAdaptacao.models import Etapa,PedidoAdaptacao, Avaliacao, Adaptacao, Diagramacao, Esteriotipia, Encadernacao, Revisao, Impressao, Transcricao
# Register your models here.

class EtapaAdmin(admin.ModelAdmin):
    pass

class EtapaInline(admin.StackedInline):
    autocomplete_fields = ['profissional']
    model = Etapa
    extra = 1

class AdaptacaoInline(admin.StackedInline):
    autocomplete_fields = ['profissional']
    model = Adaptacao
    extra = 0

class DiagramacaoInline(admin.StackedInline):
    autocomplete_fields = ['profissional']
    model = Diagramacao
    extra = 0

class EsteriotipiaInline(admin.StackedInline):
    autocomplete_fields = ['profissional']
    model = Esteriotipia
    extra = 0

class EncadernacaoInline(admin.StackedInline):
    autocomplete_fields = ['profissional']
    model = Encadernacao
    extra = 0

class RevisaoInline(admin.StackedInline):
    autocomplete_fields = ['profissional']
    model = Revisao
    extra = 0

class ImpressaoInline(admin.StackedInline):
    autocomplete_fields = ['profissional']
    model = Impressao
    extra = 0

class TranscricaoInline(admin.StackedInline):
    autocomplete_fields = ['profissional']
    model = Transcricao
    extra = 0

class RevisaoInline(admin.StackedInline):    
    model = Revisao
    extra = 0

class AdaptacaoAdmin(admin.ModelAdmin):
    autocomplete_fields = ['profissional']

class DiagramacaoAdmin(admin.ModelAdmin):
    autocomplete_fields = ['profissional']

class EsteriotipiaAdmin(admin.ModelAdmin):
    autocomplete_fields = ['profissional']

class EncadernacaoAdmin(admin.ModelAdmin):
    autocomplete_fields = ['profissional']

class RevisaoAdmin(admin.ModelAdmin):
    autocomplete_fields = ['profissional']

class ImpressaoAdmin(admin.ModelAdmin):
    autocomplete_fields = ['profissional']

class TranscricaoAdmin(admin.ModelAdmin):
    autocomplete_fields = ['profissional']
    inlines = [RevisaoInline]

class PedidoAdaptacaoAdmin(admin.ModelAdmin):
    inlines = [TranscricaoInline, AdaptacaoInline, DiagramacaoInline, EsteriotipiaInline, EncadernacaoInline, ImpressaoInline]
    search_fields = ['solicitante']
    autocomplete_fields = ['solicitante','material']
 

admin.site.register(PedidoAdaptacao, PedidoAdaptacaoAdmin)
admin.site.register(Etapa, EtapaAdmin)
admin.site.register(Adaptacao,AdaptacaoAdmin)
admin.site.register(Diagramacao,DiagramacaoAdmin)
admin.site.register(Esteriotipia,EsteriotipiaAdmin)
admin.site.register(Encadernacao,EncadernacaoAdmin)
admin.site.register(Revisao,RevisaoAdmin)
admin.site.register(Impressao,ImpressaoAdmin)
admin.site.register(Transcricao,TranscricaoAdmin)