from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import RegistroEnvioPedidosForm
from .models import Pedido

# Create your views here.

def index():
    pass

@login_required
def registro_envio_pedido_registration(request):
    pedidos = Pedido.objects.all()
    
    if request.method == 'Post':
        pass
    registro_envio_pedidos_form = RegistroEnvioPedidosForm(request.POST, prefix='registro_envio_pedidos')

    return render(request, 'register_envio_pedido.html',{
        'registro_envio_pedidos_form' : registro_envio_pedidos_form,
    })