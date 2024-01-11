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
    titulo = models.CharField(max_length = 255, null = True)
    acervo = models.CharField(max_length = 255)
    tiragem = models.CharField(max_length = 255)
    quantidade_paginas = models.PositiveIntegerField()
    arquivo_original = models.FileField(upload_to="arquivos/%Y/%m")
    def __str__(self):
        return f"{self.titulo}, {self.tipo}"
        

class MaterialBraille(models.Model):
    material = models.OneToOneField(Material, on_delete=models.CASCADE)
    quantidade_paginas_braille = models.PositiveIntegerField()
    partes = models.PositiveIntegerField()
    is_disponivel_para_assinatura = models.BooleanField(default=False)
    is_disponivel_para_pedido = models.BooleanField(default=False)
    arquivo_braille = models.FileField(upload_to="arquivos/braille/%Y/%m")
    def __str__(self):
        return self.material.__str__() + ' | Braille'

class MaterialAmpliado(models.Model):
    material = models.OneToOneField(Material, on_delete=models.CASCADE)
    quantidade_paginas_ampliada = models.PositiveIntegerField()
    partes = models.PositiveIntegerField()    
    is_disponivel_para_assinatura = models.BooleanField(default=False, verbose_name="disponibilizar para assinatura?")
    is_disponivel_para_pedido = models.BooleanField(default=False, verbose_name="disponibilizar para pedido?")
    arquivo_ampliado = models.FileField(upload_to="arquivos/ampliado/%Y/%m")
