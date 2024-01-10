from django.db import models

# Create your models here.

class Material(models.Model):
    TIPO_CHOICES = {
        "didático":"didático",
        "paradidático":"paradidático",
        "revista":"revista",
        "DAL (S/Revisão)":"DAL (S/Revisão)",
        "Outro":"Outro",
    }
    tipo = models.CharField(max_length = 255, choices=TIPO_CHOICES)
    acervo = models.CharField(max_length = 255)
    tiragem = models.CharField(max_length = 255)
    quantidade_paginas = models.PositiveIntegerField()
    arquivo_original = models.FileField(upload_to="arquivos/%Y/%m")
    is_disponivel_para_assinatura = models.BooleanField(default=False)
    is_disponivel_para_pedido = models.BooleanField(default=False)    

class MaterialBraille(Material, models.Model):
    arquivo_braille = models.FileField(upload_to="arquivos/braille/%Y/%m")
    quantidade_paginas_braille = models.PositiveIntegerField()
    partes = models.PositiveIntegerField()

class MaterialAmpliado(Material, models.Model):
    quantidade_paginas_ampliada = models.PositiveIntegerField()
    arquivo_braille = models.FileField(upload_to="arquivos/ampliado/%Y/%m")
    partes = models.PositiveIntegerField()    

