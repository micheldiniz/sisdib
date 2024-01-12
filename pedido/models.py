from django.db import models
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
    items = models.ManyToManyField(Item)
    data_registro = models.DateTimeField(auto_now_add=True)
    
