from typing import Any
from django.contrib import admin
from django.db.models.fields.related import ForeignKey
from django.forms.models import ModelChoiceField
from django.http import HttpRequest
from pedido.models import Pedido, ItemPedido, RegistroEnvioPedidos
from django.db.models import Q
from django.utils.safestring import mark_safe
from django.shortcuts import render

# Register your models here.

class ItemPedidoInline(admin.StackedInline):
    model = ItemPedido
    extra = 0
    search_fields = ['material_titulo','material_tipo']    
    autocomplete_fields = ['material']


    def formfield_for_foreignkey(self, db_field: ForeignKey[Any], request: HttpRequest | None, **kwargs: Any) -> ModelChoiceField | None:
        if db_field.name == 'material':
            qs = super().formfield_for_foreignkey(db_field, request, **kwargs).queryset
            
            object_id = request.resolver_match.kwargs.get('object_id')            
            kwargs['queryset'] = qs.filter(Q(is_disponivel_para_pedido=True)).distinct()
            
            if(object_id):                            
                pedido = Pedido.objects.get(pk=object_id)
                related_items = pedido.itens_pedido.all()                
                materiais = [item.material for item in related_items]                     
                my_qs_filter = Q(is_disponivel_para_pedido = True)                
                for material in materiais:
                    my_qs_filter = my_qs_filter | Q(material__materialadaptado = material) | Q(is_disponivel_para_pedido = True)
                
                kwargs['queryset'] = qs.filter(my_qs_filter).distinct()        
                return super().formfield_for_foreignkey(db_field, request, **kwargs)
            
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class PedidoAdmin(admin.ModelAdmin):
    inlines = [ItemPedidoInline]
    # autocomplete_fields = ('solicitante',)
    search_fields = ['numero_pedido', 'data_registro','registro_envio__descricao','estado_do_pedido']
    list_display = ['numero_pedido','data_registro','registro_envio','estado_do_pedido','solicitante','itens_do_pedido','total']
    list_editable = ['estado_do_pedido','registro_envio']
    # exclude = ['registro_envio']

    def itens_do_pedido(self, obj):
        items = obj.itens_pedido.all()
        items_list = [f'<b>Material</b>: {item.material} | <b>quantidade</b>: {item.quantidade}<br>' for item in items]
        if(len(items_list) > 0):
            items_str = ''
            for item in items_list:
                items_str += item
            return mark_safe(str(items_str))            
        return 'Nenhum item encontrado'
    
    def total(self, obj):
        items = obj.itens_pedido.all()
        return sum(obj.quantidade for obj in items)

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

class PedidoInline(admin.StackedInline):
    model = Pedido
    extra = 0

class RegistroEnvioPedidosAdmin(admin.ModelAdmin):
    search_fields = ['descricao', 'pedidos']
    list_display = ['descricao', 'data_envio', 'get_pedidos', 'estado_envio', 'observacao', 'data_registro']
    list_editable = ['estado_envio']
    # inlines = [PedidoInline]
    actions = ['get_guia_correios']

    def get_pedidos(self, obj):
        pedidos = Pedido.objects.filter(registro_envio=obj)
        links = []
        for pedido in pedidos:
            link = '<li><a href="{0}">{1}</a></li>'.format(pedido.get_admin_url(), str(pedido))
            links.append(link)
        
        print(pedidos)

        html_content = ''.join(links)
        html_content = '<ul>' + html_content + '</ul>'
        return mark_safe(html_content)
    
    
    def get_guia_correios(self, request, queryset):
        dict = {}
        for p in queryset:
            dict[p.descricao] = { 'pedidos' : Pedido.objects.filter(registro_envio = p).distinct()}
            
        print(dict)
        return render(request, 'guia_correios_pedidos.html', {
            'registroSaidaPedidos': dict,            
            })
    
    get_guia_correios.short_description = "Guia correios"
    get_pedidos.short_description = 'pedidos'

admin.site.register(RegistroEnvioPedidos, RegistroEnvioPedidosAdmin)
admin.site.register(Pedido, PedidoAdmin)