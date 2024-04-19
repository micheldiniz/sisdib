from django.urls import path
from .views import registro_envio_pedido_registration, index

urlpatterns = [
    path("", index, name="index"),
    path("cadastrar",  registro_envio_pedido_registration, name="registro_envio_pedido"),
]