from django.urls import path
from .views import success_page,pessoafisica_registration,pessoa_all, deletar_pessoa


urlpatterns = [
    path("cadastrar", pessoafisica_registration, name="pessoa_fisica_registration"),
    path("success", success_page, name="success_page"),
    path("all", pessoa_all, name="pessoa-all"),
    path("deletar/<int:id>", deletar_pessoa, name="deletar-pessoa"),
]