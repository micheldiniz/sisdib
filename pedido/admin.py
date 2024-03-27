from typing import Any
from django.contrib import admin
from django.db.models.fields import Field
from django.db.models.query import QuerySet
from django.http import HttpRequest
from pedido.models import Pedido, ItemPedido
from django.db.models import Q

# Register your models here.

class ItemPedidoInline(admin.StackedInline):
    model = ItemPedido
    extra = 1
    raw_id_fields = ('material',)
    autocomplete_fields = ('material',)
    list_display = ()

class PedidoAdmin(admin.ModelAdmin):
    inlines = [ItemPedidoInline]
    # autocomplete_fields = ('solicitante',)

    # def get_search_results(self, request: HttpRequest, queryset: QuerySet[Any], search_term: str) -> tuple[QuerySet[Any], bool]:
    #     queryset, may_have_duplicates = super().get_search_results(request, queryset, search_term)
    #     if 'solicitante' in request.GET:
    #         queryset = queryset.filter(pessoa__pessoajuridica__isnull=False)            
    #     return queryset, may_have_duplicates
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):        
        
        if db_field.name == 'solicitante':
            qs = super().formfield_for_foreignkey(db_field, request, **kwargs).queryset
            object_id = request.resolver_match.kwargs.get('object_id')
            if (object_id):
                pedido_instance = Pedido.objects.get(id=object_id)
                current_solicitante = pedido_instance.solicitante.pessoa
                filtered_qs = qs.filter(Q(pessoa__pessoajuridica__isnull=False) | Q(pessoa = current_solicitante)).distinct()

                kwargs['queryset'] = filtered_qs
                return super().formfield_for_foreignkey(db_field, request, **kwargs)
            kwargs['queryset'] = qs.filter(Q(pessoa__pessoajuridica__isnull=False)).distinct()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Pedido, PedidoAdmin)