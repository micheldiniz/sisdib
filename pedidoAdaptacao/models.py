from django.db import models
from material.models import Material
from datetime import datetime
import os

# Create your models here.

def get_material_upload_path(filename):
    date_part = datetime.now().strftime('%Y/%m')
  
    return os.path.join('etapa', date_part, filename)


class PedidoAdaptacao(models.Model):    
    class Meta:
        verbose_name_plural = 'Pedidos de adaptação'
    material = models.ForeignKey(Material, on_delete=models.CASCADE)

class Etapa(models.Model):
    ETAPA_CHOICES = [
        ('adaptação','adaptação'),
        ('diagramação','diagramação'),
        ('esteriotipia','esteriotipia'),
        ('encadernação','encadernação'),
        ('expedição','expedição'),
        ('impressão tinta','impressão tinta'),
        ('impressão braille','impressão braille'),
        ('transcrição','transcrição'),
    ]
    class Meta:
        verbose_name_plural = 'Registo de envio de Pedidos'

    nome_etapa = models.CharField(max_length=255, choices = ETAPA_CHOICES)
    data_registro = models.DateTimeField(verbose_name='Data de registro', auto_now_add=True)
    data_inicio = models.DateTimeField(verbose_name='Data de registro', blank=True)
    data_fim = models.DateTimeField(verbose_name='Data de registro', auto_now_add=True)
    profissional = models.CharField(max_length=255)
    arquivo_original = models.FileField(upload_to=get_material_upload_path, null = True, blank= True)


class Avaliacao(models.Model):
    pass

