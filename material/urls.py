from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cadastrar", views.cadastrar_Material, name="cadastrar_material"),
    path('material/<int:material_id>/download', views.download_file, name='download_file')
]