from django.db import models
from abc import ABC, abstractmethod
from material.models import Material
from pedido.models import Pedido
from pessoa.models import Pessoa

# Create your models here.

class Assinatura(models.Model):
    ESTADO_CHOICES =[
        # ('0','nenhuma'),
        ('1','vigente'),
        ('0','cancelado'),
    ]
    estado = models.CharField(max_length=2,choices=ESTADO_CHOICES, default='vigente')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, null=True)

class Cliente(models.Model):
    assinaturas = models.ManyToManyField(Assinatura)
    pedidos = models.ManyToManyField(Pedido)    
    data_registro = models.DateTimeField(auto_now_add=True)
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)

