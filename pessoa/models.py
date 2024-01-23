from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome =  models.CharField(max_length=255,null=True)
    def __str__(self) -> str:
        return f"Nome: {self.nome}"
  
class Endereco(models.Model):
    cep = models.CharField(max_length=255)
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    pessoa = models.OneToOneField(Pessoa,on_delete=models.CASCADE, default=None)

class Contato(models.Model):
    nome_contato = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    celular = models.CharField(max_length=255)
    pessoa = models.OneToOneField(Pessoa,on_delete=models.CASCADE, default=None)

class PessoaFisica(Pessoa, models.Model):    
    cpf = models.CharField(max_length=255)
    def __str__(self):
        return self.nome + ' ' + self.get_cpf()
       
    def format_cpf(self, cpf:str):
        return cpf[0:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:11]
    
    def get_cpf(self):
        return self.format_cpf(self.cpf)

class PessoaJuridica(Pessoa, models.Model):
    cnpj = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"cnpj: {self.cnpj}, {self.nome}"
