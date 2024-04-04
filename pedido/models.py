from django.db import models
from cliente.models import Cliente
from material.models import MaterialAdaptado

# Create your models here.

class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('novo','novo'),
        ('processado','processado'),
        ('enviado','enviado'),
        ('finalizado','finalizado'),
        ('pendente','pendente'),
    ]
    data_registro = models.DateTimeField(auto_now_add=True)
    numero_pedido = models.PositiveBigIntegerField()
    estado_do_pedido = models.CharField(max_length=255, choices = ESTADO_CHOICES, default = "novo")
    solicitante = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    observacao = models.CharField(max_length=255)

    def __str__(self):        
        return self.numero_pedido.__str__()

class ItemPedido(models.Model):
    ESTADO_CHOICES = [
        ("aceito","aceito"),
        ("indisponivel","indisponivel"),
        ("pendente","pendente"),
    ]
    quantidade = models.PositiveIntegerField()
    
    material = models.ForeignKey(
        MaterialAdaptado, 
        on_delete=models.CASCADE,
        # limit_choices_to={'is_disponivel_para_pedido': True}
        )
   
    estado = models.CharField(max_length=255, choices=ESTADO_CHOICES)
    observacao = models.CharField(max_length=255, null=True, blank=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens_pedido')    
   
    def __str__(self):          
        return f"{self.material} quantidade: {self.quantidade}"





