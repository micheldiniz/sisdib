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
    titulo = models.CharField(max_length = 255, null = True)
    classificacao = models.CharField(max_length = 255, choices=TIPO_CHOICES)
    acervo = models.CharField(max_length = 255)
    tiragem = models.CharField(max_length = 255)
    quantidade_paginas = models.PositiveIntegerField()
    arquivo_original = models.FileField(upload_to="arquivos/%Y/%m", null = True, blank= True)
    def __str__(self):
        return f"{self.titulo}, {self.classificacao}"

class MaterialAdaptado(models.Model):    
    MATERIAL_CHOICES = {
        "braille":"braille",
        "ampliado":"ampliado",
    }
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    tipo = models.CharField(max_length = 255, choices = MATERIAL_CHOICES)
    quantidade_paginas = models.PositiveIntegerField()
    partes = models.PositiveIntegerField()
    is_disponivel_para_assinatura = models.BooleanField(default=False, verbose_name="Disponível para assinatura?")
    is_disponivel_para_pedido = models.BooleanField(default=False, verbose_name="Disponível para pedido?")
    arquivo = models.FileField(upload_to="arquivos/braille/%Y/%m", null = True, blank= True)
    def __str__(self):
        return self.material.__str__() + ' | ' + self.tipo
