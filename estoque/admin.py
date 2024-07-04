from django.contrib import admin
from estoque.models import Estoque

# Register your models here.

class EstoqueAdmin(admin.ModelAdmin):
    pass


admin.site.register(Estoque, EstoqueAdmin)