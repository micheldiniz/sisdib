from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from cliente.models import Cliente

# Create your models here.
class Item(models.Model):
    ESTADO_CHOICES = {
        "aceito":"aceito",
        "indisponivel":"indisponivel",
        "pendente":"pendente",
    }    
    quantidade = models.PositiveIntegerField()
    material_object_id = models.IntegerField()
    material_content_type = models.ForeignKey(
        ContentType,
        on_delete = models.PROTECT,
    )
    material = GenericForeignKey(
        'material_content_type',
        'material_object_id',
    )
    estado = models.CharField(max_length=255, choices=ESTADO_CHOICES)
    observacao = models.CharField(max_length=255)
    
class Pedido(models.Model):    
    items = models.ManyToManyField(Item)
    data_registro = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
