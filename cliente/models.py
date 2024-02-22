from django.db import models
from pessoa.models import Pessoa
from material.models import MaterialAdaptado

# Create your models here.

class Cliente(models.Model):
    data_registro = models.DateTimeField(auto_now_add=True)
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.pessoa.__str__()

class Assinatura(models.Model):
    ESTADO_CHOICES =[
        ('1','vigente'),
        ('0','cancelado'),
    ]
    estado = models.CharField(max_length=2,choices=ESTADO_CHOICES, default='vigente')
    material = models.ForeignKey(MaterialAdaptado, on_delete= models.CASCADE)    
    data_registro = models.DateTimeField(auto_now_add=True)
    data_ultima_alteracao = models.DateTimeField()
    observacao = models.CharField(max_length=255, verbose_name='Observação')
    solicitante = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
class Assinante(models.Model):
    nome = models.CharField(max_length=255, verbose_name="nome da pessoa que receberá o material")
    assinatura = models.OneToOneField(Assinatura, on_delete=models.CASCADE)

    
