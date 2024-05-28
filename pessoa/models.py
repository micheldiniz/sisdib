from typing import Any
from django.db import models
from datetime import datetime
from django.utils.safestring import mark_safe

BOOL_CHOICES = ((True,"Sim"),(False,"Não"))

# Create your models here.
class Pessoa(models.Model):
    class Meta:
        verbose_name_plural = 'Pessoas'
        
    nome =  models.CharField(max_length=255,null=True)    
    data_registro = models.DateField(auto_now_add=True)
    is_estrangeiro = models.BooleanField(verbose_name="Estrageiro?", choices=BOOL_CHOICES, default=False)
    nacionalidade = models.CharField(max_length=255, null=True) 

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.data_registro = datetime.now()
        super().__init__(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.nome}"    
  
class Endereco(models.Model):
    cep = models.CharField(max_length=255)
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255, null=True, blank=True)
    bairro = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    pessoa = models.OneToOneField(Pessoa,on_delete=models.CASCADE, default=None)
    def html_endereco(self):
        html_endereco = "<span class='endereco'>{0} {1}, {2} <br /> {3} <br /> {4} {5}/{6}<br /> {7}</span>".format(self.logradouro,self.numero,self.complemento,self.bairro,self.cep,self.cidade,self.estado,self.pais)        
        if(self.pais == 'Brasil'):
            html_endereco = "<span class='endereco'>{0} {1}, {2} <br /> {3} <br /> {4} {5}/{6}</span>".format(self.logradouro,self.numero,self.complemento,self.bairro,self.cep,self.cidade,self.estado)        
            return mark_safe(html_endereco)
        return mark_safe(html_endereco)

class Contato(models.Model):
    nome_contato = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    celular = models.CharField(max_length=255)
    pessoa = models.OneToOneField(Pessoa,on_delete=models.CASCADE, default=None)

class PessoaFisica(Pessoa):
    class Meta:
        verbose_name_plural = 'Pessoas Físicas'
    cpf = models.CharField(max_length=255, null=False)
    data_nascimento = models.DateField(null=True)


class PessoaJuridica(Pessoa):
    TIPO_INSTITUICAO_CHOICES = [('Associações','Associações'),('Bibliotecas','Bibliotecas'),('Centros','Centros'),('Escolas','Escolas'),('Fundações','Fundações'),('Governo','Governo'),('Instituições','Instituições'),('Universidades','Universidades'),]
    tipo_instituicao = models.CharField(max_length=255, blank=True, null=True, choices=TIPO_INSTITUICAO_CHOICES)
    class Meta:
        verbose_name_plural = 'Pessoas Jurídicas'

    cnpj = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"cnpj: {self.cnpj}, {self.nome}"
    

class Funcionario(PessoaFisica):
    class Meta:
        verbose_name = 'funcionário'
        verbose_name_plural = 'funcionários'

    matricula = models.CharField(max_length=255, null=False)
    profissao = models.CharField(max_length=255, null=False)

    def __str__(self) -> str:
        return super().__str__() + ' ' + self.profissao

