from django.contrib import admin
from django.db.models.fields.reverse_related import ForeignObjectRel
from cliente.models import Solicitante,Assinatura,Assinante,RegistroEnvioAssinaturas
from pessoa.models import PessoaFisica, PessoaJuridica, Endereco, Contato
from django.db.models import Q
from typing import Any
from django.contrib import admin
from django.db.models.fields.related import ForeignKey
from django.forms.models import ModelChoiceField
from django.http import HttpRequest
from django.db.models import Q
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from datetime import datetime
from django.utils.safestring import mark_safe


class CustomRawIdWidget(ForeignKeyRawIdWidget):

    def __init__(self, rel: ForeignObjectRel, admin_site: admin.AdminSite, attrs: None = ..., using: None = ...) -> None:
        super().__init__(rel, admin_site, attrs, using)

    def render(self, name, value, attrs=None, renderer=None):
        rendered = super().render(name, value, attrs, renderer)
        rendered += '''
            <script>
                document.addEventListener('DOMContentLoaded', function() {
                    const selectAllLink = document.createElement('a');
                    selectAllLink.textContent = 'Select All';
                    selectAllLink.href = '#';
                    selectAllLink.onclick = function(e) {
                        e.preventDefault();
                        const rawIdInput = document.getElementById("id_" + name);
                        if (rawIdInput) {
                            const win = window.open(rawIdInput.getAttribute('assinatura'), '_blank');
                            if (win) {
                                win.onload = function() {
                                    const checkboxes = win.document.querySelectorAll('.checkbox');
                                    checkboxes.forEach(function(checkbox) {
                                        checkbox.checked = true;
                                    });
                                };
                            }
                        }
                    };
                    document.querySelector('.field-{0}').appendChild(selectAllLink);
                });
            </script>
        '''.format(name)
        return rendered

@admin.action(description='cancelar assinatura(s)')
def cancela_assinatura(modeladmin, request, queryset):
    queryset.update(estado='cancelado', observacao='Cancelamento realizado em lote', data_ultima_alteracao = datetime.now())


class AssinanteInline(admin.StackedInline):
    model = Assinante    
    extra = 0

class AssinaturaAdmin(admin.ModelAdmin):
    inlines = [AssinanteInline]
    list_display = ['material','solicitante','data_registro', 'estado', 'observacao', 'data_ultima_alteracao']
    list_editable = ['estado', 'observacao']
    search_fields = ['material__material__titulo','estado','solicitante__pessoa__nome', 'material__tipo']
    # raw_id_fields = ('material', )
    # autocomplete_fields = ('material','solicitante')
    exclude = ('data_ultima_alteracao',)
    actions = [cancela_assinatura]

    def formfield_for_foreignkey(self, db_field: ForeignKey[Any], request: HttpRequest | None, **kwargs: Any) -> ModelChoiceField | None:

        if db_field.name == 'material':
            qs = super().formfield_for_foreignkey(db_field, request, **kwargs).queryset
            object_id = request.resolver_match.kwargs.get('object_id')
            
            if (object_id):
                assinatura_instance = Assinatura.objects.get(id=object_id)
                current_material = assinatura_instance.material
                filtered_qs = qs.filter(Q(is_disponivel_para_assinatura=True) | Q(material__materialadaptado = current_material)).distinct()
                kwargs['queryset'] = filtered_qs

                return super().formfield_for_foreignkey(db_field, request, **kwargs)

            filtered_qs = qs.filter(Q(is_disponivel_para_assinatura=True)).distinct()
            kwargs['queryset'] = filtered_qs
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class SolicitanteAdmin(admin.ModelAdmin):
    search_fields = ['pessoa__nome','pessoa__nacionalidade', 'pessoa__endereco__pais']
    list_display = ['pessoa', 'assinaturas_ativas', 'assinaturas_canceladas']

    def assinaturas_ativas(self, obj):
        assinaturas = Assinatura.objects.filter(solicitante=obj, estado='vigente')
        if assinaturas.count() < 1:
            return 'nenhuma'
        assinaturas_html = []
        for assinatura in assinaturas:
            html = '<a href="{0}">{1}</a></br>'.format(assinatura.get_admin_url(),str(assinatura.material))
            assinaturas_html.append(html)
        html_content = ''.join(assinaturas_html)
        return mark_safe(html_content)

    def assinaturas_canceladas(self, obj):
        assinaturas = Assinatura.objects.filter(solicitante=obj, estado='cancelado')
        if assinaturas.count() < 1:
            return 'nenhuma'
        assinaturas_html = []
        for assinatura in assinaturas:
            html = '<a href="{0}">{1}</a></br>'.format(assinatura.get_admin_url(),str(assinatura.material))
            assinaturas_html.append(html)
        html_content = ''.join(assinaturas_html)
        return mark_safe(html_content)

class RegistroEnvioAssinaturasAdmin(admin.ModelAdmin):
    search_fields = ['descricao', 'assinaturas']
    list_display = ['descricao','data_envio','get_total_assinaturas','data_registro', 'observacao']
    # raw_id_fields = ['assinaturas']
    autocomplete_fields = ['assinaturas']
    # formfield_overrides = {
    #     models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    # }
    # formfield_overrides = {
    #     models.ManyToManyField: {'widget': CustomRawIdWidget},
    # }
    def get_assinaturas(self, obj):
        return "\n".join([str(p) for p in obj.assinaturas.all()])
    
    def get_total_assinaturas(self, obj):
        return obj.assinaturas.count()

    get_assinaturas.short_description = 'Assinaturas enviadas'
    get_total_assinaturas.short_description = 'Total de assinaturas enviadas'


admin.site.register(Solicitante, SolicitanteAdmin)
admin.site.register(Assinatura, AssinaturaAdmin)
admin.site.register(RegistroEnvioAssinaturas, RegistroEnvioAssinaturasAdmin)

