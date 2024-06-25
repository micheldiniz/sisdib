from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cadastrar", views.cadastrar_material, name="cadastrar_material"),
    # path("visualizar", views.visualizar_material, name="visualizar_material"),
    path("todos", views.list_materiais, name="list_materials"),
    path("adaptado/cadastrar", views.cadastrar_material_adaptado, name="cadastrar_material_adaptado"),
    path("<int:id>", views.visualizar_material, name="visualizar_material"),
    path("adaptado/<int:id>", views.visualizar_material_adaptado, name="visualizar_material_adaptado"),
    path("editar/<int:id>", views.editar_material, name="editar_material"),
    path("adaptado/editar/<int:id>", views.editar_material_adaptado, name="editar_material_adaptado"),
    path("adaptado/todos", views.list_materiais_adaptados, name="list_materials_adaptados"),
    path('material/<int:material_id>/download', views.download_file, name='download_file')
]