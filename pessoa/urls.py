from django.urls import path
from .views import success_page,pessoafisica_registration

urlpatterns = [
    path("cadastrar", pessoafisica_registration, name="pessoa_fisica_registration"),
    path("success/", success_page, name="success_page"),
]