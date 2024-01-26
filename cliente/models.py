from django.db import models
from abc import ABC, abstractmethod
from material.models import Material
from pedido.models import Pedido
from pessoa.models import Pessoa
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class Assinatura(models.Model):
    ESTADO_CHOICES =[
        # ('0','nenhuma'),
        ('1','vigente'),
        ('0','cancelado'),
    ]
    estado = models.CharField(max_length=2,choices=ESTADO_CHOICES, default='vigente')
    # material = models.ForeignKey(Material, on_delete=models.CASCADE, null=True)
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

class Cliente(models.Model):
    assinaturas = models.ManyToManyField(Assinatura)
    pedidos = models.ManyToManyField(Pedido)    
    data_registro = models.DateTimeField(auto_now_add=True)
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)

