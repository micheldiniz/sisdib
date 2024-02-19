from django.db import models
from cliente.models import Cliente
from material.models import MaterialAdaptado

# Create your models here.

class Pedido(models.Model):        
    data_registro = models.DateTimeField(auto_now_add=True)
    numero_pedido = models.PositiveBigIntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):        
        return self.numero_pedido.__str__()

class ItemPedido(models.Model):
    ESTADO_CHOICES = {
        "aceito":"aceito",
        "indisponivel":"indisponivel",
        "pendente":"pendente",
    }
    quantidade = models.PositiveIntegerField()
    
    material = models.ForeignKey(MaterialAdaptado, on_delete=models.CASCADE)
   
    estado = models.CharField(max_length=255, choices=ESTADO_CHOICES)
    observacao = models.CharField(max_length=255)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)    
   
    def __str__(self):  
        obj =  self.getGenericObject() 
        return f"{obj.__str__()} quantidade: {self.quantidade}"
