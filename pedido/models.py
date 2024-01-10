from django.db import models
from cliente.models import Cliente
from material.models import Material

# Create your models here.
class Item(models.Model):
    ESTADO_CHOICES = {
        "aceito":"aceito",
        "indisponivel":"indisponivel",
        "pendente":"pendente",
    }    
    quantidade = models.PositiveIntegerField()
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    estado = models.CharField(max_length=255, choices=ESTADO_CHOICES)
    observacao = models.CharField(max_length=255)
    
class Pedido(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    

