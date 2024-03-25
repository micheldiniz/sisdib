from django.db import models
import os
from datetime import datetime
# Create your models here.

def get_material_upload_path(instance, filename):
    date_part = datetime.now().strftime('%Y/%m')

    if isinstance(instance, MaterialAdaptado):
        return os.path.join('materiais',instance.tipo, date_part,filename)
    return os.path.join('materiais', date_part, filename)
class Material(models.Model):
    class Meta:
        verbose_name_plural = 'Materiais'

    TIPO_CHOICES = [
        ("didático","didático"),
        ("paradidático","paradidático"),
        ("revista","revista"),
        ("DAL (S/Revisão)","DAL (S/Revisão)"),
        ("Outro","Outro"),
    ]
    classificacao = models.CharField(max_length = 255, null = True, choices = TIPO_CHOICES)
    titulo = models.CharField(max_length = 255)
    autor =  models.CharField(max_length = 255, null=True, blank=True)
    edicao = models.CharField(max_length = 255, null=True, blank=True)
    editora = models.CharField(max_length = 255, null=True, blank=True)
    publico_alvo = models.CharField(max_length = 255, null=True, blank=True, verbose_name = 'Público alvo')
    acervo = models.CharField(max_length = 255, null=True, blank=True)
    tiragem = models.CharField(max_length = 255, null=True, blank=True)
    quantidade_paginas = models.PositiveIntegerField(null=True, blank=True)
    arquivo_original = models.FileField(upload_to=get_material_upload_path, null = True, blank= True)
    def __str__(self):
        return f'{self.titulo}, {self.classificacao}'

class MaterialAdaptado(models.Model):    
    class Meta:
        verbose_name_plural = 'Materiais Adaptados'
        
    MATERIAL_CHOICES = [
        ("braille","braille"),
        ("ampliado","ampliado"),
    ]
    
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    tipo = models.CharField(max_length = 255, choices = MATERIAL_CHOICES)
    quantidade_paginas = models.PositiveIntegerField(blank=True, null = True)
    partes = models.PositiveIntegerField(blank=True, null = True)
    arquivo = models.FileField(upload_to=get_material_upload_path, null = True, blank= True)
    is_disponivel_para_pedido = models.BooleanField(default=False, verbose_name="Disponível para pedido?")
    is_disponivel_para_assinatura = models.BooleanField(default=False, verbose_name="Disponível para assinatura?")
    
    def __str__(self):
        return f'{self.material} ({self.tipo})'
