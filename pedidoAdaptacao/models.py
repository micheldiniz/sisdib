from django.db import models
from material.models import Material
from datetime import datetime
from cliente.models import Solicitante
import os

# Create your models here.

def get_material_upload_path(filename):
    date_part = datetime.now().strftime('%Y/%m')  
    return os.path.join('etapa', date_part, filename)

class PedidoAdaptacao(models.Model):    
    class Meta:
        verbose_name_plural = 'Pedidos de adaptação'
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    solicitante = models.ForeignKey(Solicitante,on_delete=models.CASCADE)
    data_registro = models.DateTimeField(verbose_name='Data de registro', auto_now_add=True)
    descricao = models.CharField(max_length=500, verbose_name='descrição')
    

class Etapa(models.Model):
    ETAPA_CHOICES = [
        ('adaptação','adaptação'),
        ('diagramação','diagramação'),
        ('esteriotipia','esteriotipia'),
        ('encadernação','encadernação'),
        ('expedição','expedição'),
        ('revisão','revisão'),
        ('impressão tinta','impressão tinta'),
        ('impressão braille','impressão braille'),
        ('transcrição','transcrição'),
    ]
    class Meta:
        verbose_name_plural = 'Etapas'

    nome_etapa = models.CharField(max_length=255, choices = ETAPA_CHOICES)
    data_registro = models.DateTimeField(verbose_name='Data de registro', auto_now_add=True)
    data_inicio = models.DateField(verbose_name='Data de início')
    data_fim = models.DateField(verbose_name='Data de finalização')
    profissional = models.CharField(max_length=255)
    arquivo_original = models.FileField(upload_to=get_material_upload_path, null = True, blank= True)
    pedido_adaptacao = models.ForeignKey(to=PedidoAdaptacao, on_delete=models.CASCADE)

#class para avaliação de atendimento de pedido
class Avaliacao(models.Model):
    pass

#classe para revisao de pedido
class Revisao(models.Model):
    class Meta:
        verbose_name_plural = 'Revisões'
    profissional = models.CharField(max_length=255)
    arquivo_revisado = models.FileField(upload_to=get_material_upload_path, null = True, blank= True)
    

class Adaptacao(models.Model):
    class Meta:
        verbose_name_plural = 'Adaptações'
    pedido_adaptacao = models.ForeignKey(PedidoAdaptacao, on_delete=models.CASCADE)
    data_registro = models.DateTimeField(verbose_name='Data de registro', auto_now_add=True)
    data_inicio = models.DateField(verbose_name='Data de início')
    data_fim = models.DateField(verbose_name='Data de finalização')
    profissional = models.CharField(max_length=255)
    arquivo_adaptado = models.FileField(upload_to=get_material_upload_path, null = True, blank= True)


class Diagramacao(models.Model):
    class Meta:
        verbose_name_plural = 'Diagramações'
    pedido_adaptacao = models.ForeignKey(PedidoAdaptacao, on_delete=models.CASCADE)
    data_registro = models.DateTimeField(verbose_name='Data de registro', auto_now_add=True)
    data_inicio = models.DateField(verbose_name='Data de início')
    data_fim = models.DateField(verbose_name='Data de finalização')
    profissional = models.CharField(max_length=255)
    arquivo_diagramado = models.FileField(upload_to=get_material_upload_path, null = True, blank= True)


class Esteriotipia(models.Model):
    class Meta:
        verbose_name_plural = 'Esteriotipias'
    pedido_adaptacao = models.ForeignKey(PedidoAdaptacao, on_delete=models.CASCADE)
    data_registro = models.DateTimeField(verbose_name='Data de registro', auto_now_add=True)
    data_inicio = models.DateField(verbose_name='Data de início')
    data_fim = models.DateField(verbose_name='Data de finalização')
    profissional = models.CharField(max_length=255)

class Encadernacao(models.Model):
    class Meta:
        verbose_name_plural = 'Encadernações'
    pedido_adaptacao = models.ForeignKey(PedidoAdaptacao, on_delete=models.CASCADE)
    data_registro = models.DateTimeField(verbose_name='Data de registro', auto_now_add=True)
    data_inicio = models.DateField(verbose_name='Data de início')
    data_fim = models.DateField(verbose_name='Data de finalização')
    profissional = models.CharField(max_length=255)

class Impressao(models.Model):
    TIPO_IMPRESSAO_CHOICES = [
        ('BRAILLE','BRAILLE'),
        ('AMPLIADO','AMPLIADO'),
    ]
    class Meta:
        verbose_name_plural = 'Impressões'
    tipo_impressao = models.CharField(max_length=255, choices=TIPO_IMPRESSAO_CHOICES)
    pedido_adaptacao = models.ForeignKey(PedidoAdaptacao, on_delete=models.CASCADE)
    data_registro = models.DateTimeField(verbose_name='Data de registro', auto_now_add=True)
    data_inicio = models.DateField(verbose_name='Data de início')
    data_fim = models.DateField(verbose_name='Data de finalização')
    quantidade_paginas_impressas = models.PositiveIntegerField(verbose_name='qunatidade de páginas impressas')
    profissional = models.CharField(max_length=255)

class Transcricao(models.Model):
    class Meta:
        verbose_name_plural = 'Transcrições'
    pedido_adaptacao = models.ForeignKey(PedidoAdaptacao, on_delete=models.CASCADE)
    data_registro = models.DateTimeField(verbose_name='Data de registro', auto_now_add=True)
    data_inicio = models.DateField(verbose_name='Data de início')
    data_fim = models.DateField(verbose_name='Data de finalização')
    profissional = models.CharField(max_length=255)
    arquivo_transcrito = models.FileField(upload_to=get_material_upload_path, null = True, blank= True)
    