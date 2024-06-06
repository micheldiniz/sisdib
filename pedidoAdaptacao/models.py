from django.db import models
from material.models import Material
from datetime import datetime
from assinatura.models import Solicitante
from pessoa.models import Funcionario
import os

# Create your models here.

def get_material_upload_path(filename):
    date_part = datetime.now().strftime('%Y/%m')  
    return os.path.join('etapa', date_part, filename)

ESTADO_CHOICES = [
    ('novo','novo'),
    ('processado','processado'), 
    ('pendente','pendente'),
    ('finalizado','finalizado'),
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

class Adaptacao(models.Model):
    class Meta:
        verbose_name_plural = 'Adaptações'
    estado_adaptacao = models.CharField(max_length=255, choices = ESTADO_CHOICES, default = "novo", verbose_name="estado da adaptação")
    data_registro = models.DateTimeField(verbose_name='Data de registro', auto_now_add=True)
    data_inicio = models.DateField(verbose_name='Data de início')
    data_fim = models.DateField(verbose_name='Data de finalização')
    profissional = models.ForeignKey(Funcionario, on_delete= models.CASCADE)
    arquivo_adaptado = models.FileField(upload_to=get_material_upload_path, null = True, blank= True)
    pedido_adaptacao = models.ForeignKey(PedidoAdaptacao, on_delete=models.CASCADE)

class Diagramacao(models.Model):
    class Meta:
        verbose_name_plural = 'Diagramações'
    estado_diagramacao = models.CharField(max_length=255, choices = ESTADO_CHOICES, default = "novo", verbose_name="estado da diagramação")
    data_registro = models.DateTimeField(verbose_name='Data de registro', auto_now_add=True)
    data_inicio = models.DateField(verbose_name='Data de início')
    data_fim = models.DateField(verbose_name='Data de finalização')
    profissional = models.ForeignKey(Funcionario, on_delete= models.CASCADE)
    arquivo_diagramado = models.FileField(upload_to=get_material_upload_path, null = True, blank= True)
    pedido_adaptacao = models.ForeignKey(PedidoAdaptacao, on_delete=models.CASCADE)

class Esteriotipia(models.Model):
    class Meta:
        verbose_name_plural = 'Esteriotipias'
    estado_esteriotipia = models.CharField(max_length=255, choices = ESTADO_CHOICES, default = "novo", verbose_name="estado da esteriotipia")
    data_registro = models.DateTimeField(verbose_name='Data de registro', auto_now_add=True)
    data_inicio = models.DateField(verbose_name='Data de início')
    data_fim = models.DateField(verbose_name='Data de finalização')
    profissional = models.ForeignKey(Funcionario, on_delete= models.CASCADE)
    pedido_adaptacao = models.ForeignKey(PedidoAdaptacao, on_delete=models.CASCADE)

class Encadernacao(models.Model):
    class Meta:
        verbose_name_plural = 'Encadernações'
    estado_encadernacao = models.CharField(max_length=255, choices = ESTADO_CHOICES, default = "novo", verbose_name="estado da encadernação")
    data_registro = models.DateTimeField(verbose_name='Data de registro', auto_now_add=True)
    data_inicio = models.DateField(verbose_name='Data de início')
    data_fim = models.DateField(verbose_name='Data de finalização')
    profissional = models.ForeignKey(Funcionario, on_delete= models.CASCADE)
    pedido_adaptacao = models.ForeignKey(PedidoAdaptacao, on_delete=models.CASCADE)

class Impressao(models.Model):
    TIPO_IMPRESSAO_CHOICES = [
        ('BRAILLE','BRAILLE'),
        ('AMPLIADO','AMPLIADO'),
    ]
    class Meta:
        verbose_name_plural = 'Impressões'
    estado_impressao = models.CharField(max_length=255, choices = ESTADO_CHOICES, default = "novo", verbose_name="estado da impressão")
    tipo_impressao = models.CharField(max_length=255, choices=TIPO_IMPRESSAO_CHOICES)
    data_registro = models.DateTimeField(verbose_name='Data de registro', auto_now_add=True)
    data_inicio = models.DateField(verbose_name='Data de início')
    data_fim = models.DateField(verbose_name='Data de finalização')
    quantidade_paginas_impressas = models.PositiveIntegerField(verbose_name='quantidade de páginas impressas')
    profissional = models.ForeignKey(Funcionario, on_delete= models.CASCADE)
    pedido_adaptacao = models.ForeignKey(PedidoAdaptacao, on_delete=models.CASCADE)

class Transcricao(models.Model):
    class Meta:
        verbose_name_plural = 'Transcrições'
    estado_transcricao = models.CharField(max_length=255, choices = ESTADO_CHOICES, default = "novo", verbose_name="estado da transcrição")
    data_registro = models.DateTimeField(verbose_name='Data de registro', auto_now_add=True)
    data_inicio = models.DateField(verbose_name='Data de início')
    data_fim = models.DateField(verbose_name='Data de finalização')
    profissional = models.ForeignKey(Funcionario, on_delete= models.CASCADE)
    arquivo_transcrito = models.FileField(upload_to=get_material_upload_path, null = True, blank= True)
    pedido_adaptacao = models.ForeignKey(PedidoAdaptacao, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return 'Transcrição ' + self.id.__str__()

class Revisao(models.Model):
    REVISAO_CHOICES = [
        ('novo','novo'),
        ('aprovado','aprovado'),
        ('recusado','recusado'),
    ]
    class Meta:
        verbose_name_plural = 'Revisões'        
    profissional = models.ForeignKey(Funcionario, on_delete= models.CASCADE)
    data_registro = models.DateTimeField(verbose_name='Data de registro', auto_now_add=True)
    data_inicio = models.DateField(verbose_name='Data de início', null = True, blank= True)
    data_fim = models.DateField(verbose_name='Data de finalização', null = True, blank= True)
    arquivo_revisado = models.FileField(upload_to=get_material_upload_path, null = True, blank= True)
    estado_revisao = models.CharField(max_length=255, choices = REVISAO_CHOICES, default = "novo")
    transcricao = models.ForeignKey(Transcricao, on_delete= models.CASCADE)