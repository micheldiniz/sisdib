from django.db import models
from pessoa.models import Pessoa
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class Cliente(models.Model):
    data_registro = models.DateTimeField(auto_now_add=True)
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)

class Assinatura(models.Model):
    ESTADO_CHOICES =[
        ('1','vigente'),
        ('0','cancelado'),
    ]
    estado = models.CharField(max_length=2,choices=ESTADO_CHOICES, default='vigente')
    material_object_id = models.IntegerField()
    material_content_type = models.ForeignKey(
        ContentType,
        on_delete = models.PROTECT,
    )
    material = GenericForeignKey(
        'material_content_type',
        'material_object_id',
    )
    observacao = models.CharField(max_length=255, verbose_name='Observação')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    
