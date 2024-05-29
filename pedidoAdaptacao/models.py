from django.db import models
from material.models import Material
from datetime import datetime
from cliente.models import Solicitante
from pessoa.models import Funcionario
import os

# Create your models here.

def get_material_upload_path(filename):
    date_part = datetime.now().strftime('%Y/%m')  
    return os.path.join('etapa', date_part, filename)

ESTADO_CHOICES = [
    ('novo','novo'),
    ('processado','processado'), 
    ('finalizado','finalizado'),
    ('pendente','pendente'),
]

class PedidoAdaptacao(models.Model):    
    class Meta:
        verbose_name_plural = 'Pedidos de adaptação'
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    solicitante = models.ForeignKey(Solicitante,on_delete=models.CASCADE)
    data_registro = models.DateTimeField(verbose_name='Data de registro', auto_now_add=True)
    quantidade_solicitada = models.PositiveIntegerField(blank=True, null=True)
    descricao = models.CharField(max_length=500, verbose_name='descrição')
    
    def __str__(self):
        return 'nº: ' + str(self.id) + ' ' + self.solicitante.pessoa.nome + ', ' + self.material.__str__()

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
    profissional = models.ForeignKey(Funcionario, on_delete= models.CASCADE)
    arquivo_original = models.FileField(upload_to=get_material_upload_path, null = True, blank= True)
    pedido_adaptacao = models.ForeignKey(to=PedidoAdaptacao, on_delete=models.CASCADE)

#class para avaliação de atendimento de pedido
class Avaliacao(models.Model):
    pass

#classe para revisao de pedido
class Revisao(models.Model):
    class Meta:
        verbose_name_plural = 'Revisões'
    profissional = models.ForeignKey(Funcionario, on_delete= models.CASCADE)
    arquivo_revisado = models.FileField(upload_to=get_material_upload_path, null = True, blank= True)
    estado_envio = models.CharField(max_length=255, choices = ESTADO_CHOICES, default = "novo")   

class Adaptacao(models.Model):
    class Meta:
        verbose_name_plural = 'Adaptações'
    pedido_adaptacao = models.ForeignKey(PedidoAdaptacao, on_delete=models.CASCADE)
    data_registro = models.DateTimeField(verbose_name='Data de registro', auto_now_add=True)
    data_inicio = models.DateField(verbose_name='Data de início')
    data_fim = models.DateField(verbose_name='Data de finalização')
    profissional = models.ForeignKey(Funcionario, on_delete= models.CASCADE)
    arquivo_adaptado = models.FileField(upload_to=get_material_upload_path, null = True, blank= True)
    estado_envio = models.CharField(max_length=255, choices = ESTADO_CHOICES, default = "novo")   

class Diagramacao(models.Model):
    class Meta:
        verbose_name_plural = 'Diagramações'
    pedido_adaptacao = models.ForeignKey(PedidoAdaptacao, on_delete=models.CASCADE)
    data_registro = models.DateTimeField(verbose_name='Data de registro', auto_now_add=True)
    data_inicio = models.DateField(verbose_name='Data de início')
    data_fim = models.DateField(verbose_name='Data de finalização')
    profissional = models.ForeignKey(Funcionario, on_delete= models.CASCADE)
    arquivo_diagramado = models.FileField(upload_to=get_material_upload_path, null = True, blank= True)
    estado_envio = models.CharField(max_length=255, choices = ESTADO_CHOICES, default = "novo")   

class Esteriotipia(models.Model):
    class Meta:
        verbose_name_plural = 'Esteriotipias'
    pedido_adaptacao = models.ForeignKey(PedidoAdaptacao, on_delete=models.CASCADE)
    data_registro = models.DateTimeField(verbose_name='Data de registro', auto_now_add=True)
    data_inicio = models.DateField(verbose_name='Data de início')
    data_fim = models.DateField(verbose_name='Data de finalização')
    profissional = models.ForeignKey(Funcionario, on_delete= models.CASCADE)
    estado_envio = models.CharField(max_length=255, choices = ESTADO_CHOICES, default = "novo")   

class Encadernacao(models.Model):
    class Meta:
        verbose_name_plural = 'Encadernações'
    pedido_adaptacao = models.ForeignKey(PedidoAdaptacao, on_delete=models.CASCADE)
    data_registro = models.DateTimeField(verbose_name='Data de registro', auto_now_add=True)
    data_inicio = models.DateField(verbose_name='Data de início')
    data_fim = models.DateField(verbose_name='Data de finalização')
    profissional = models.ForeignKey(Funcionario, on_delete= models.CASCADE)
    estado_envio = models.CharField(max_length=255, choices = ESTADO_CHOICES, default = "novo")   

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
    profissional = models.ForeignKey(Funcionario, on_delete= models.CASCADE)
    estado_envio = models.CharField(max_length=255, choices = ESTADO_CHOICES, default = "novo")   

class Transcricao(models.Model):
    class Meta:
        verbose_name_plural = 'Transcrições'
    pedido_adaptacao = models.ForeignKey(PedidoAdaptacao, on_delete=models.CASCADE)
    data_registro = models.DateTimeField(verbose_name='Data de registro', auto_now_add=True)
    data_inicio = models.DateField(verbose_name='Data de início')
    data_fim = models.DateField(verbose_name='Data de finalização')
    profissional = models.ForeignKey(Funcionario, on_delete= models.CASCADE)
    arquivo_transcrito = models.FileField(upload_to=get_material_upload_path, null = True, blank= True)
    estado_envio = models.CharField(max_length=255, choices = ESTADO_CHOICES, default = "novo")
