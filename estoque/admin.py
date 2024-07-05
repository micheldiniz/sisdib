from django.contrib import admin
from estoque.models import EntradaEstoque

# Register your models here.

class EntradaEstoqueAdmin(admin.ModelAdmin):
    pass


admin.site.register(EntradaEstoque, EntradaEstoqueAdmin)