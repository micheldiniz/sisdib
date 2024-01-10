from django.db import models
from abc import ABC, abstractmethod

# Create your models here.
class Endereco(models.Model):
    cep = models.CharField(max_length=255)
    logradouro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255)

class Contato(models.Model):
    email = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    nome_contato = models.CharField(max_length=255)
    celular = models.CharField(max_length=255)

class Assinatura(models.Model):
    ESTADO_CHOICES =[
        ('0','nenhuma'),
        ('1','cancelado'),
        ('2','vigente'),
    ]
    estado = models.CharField(max_length=2,choices=ESTADO_CHOICES)

class Cliente(models.Model):
    nome =  models.CharField(max_length=255,null=True)
    assinatura = models.OneToOneField(Assinatura, on_delete=models.CASCADE)
    contato = models.OneToOneField(Contato, on_delete=models.CASCADE, null=True)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, null=True)
    data_registro = models.DateTimeField(auto_now_add=True)
   
class PessoaFisica(Cliente, models.Model):
    cpf = models.CharField(max_length=255)
    def __str__(self):
        return self.nome + ' ' + self.get_cpf()
       
    def format_cpf(self, cpf:str):
        return cpf[0:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:11]
    
    def get_cpf(self):
        return self.format_cpf(self.cpf)
        

class PessoaJuridica(Cliente, models.Model):
    cnpj = models.CharField(max_length=255)    
 

