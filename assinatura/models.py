from django.db import models
from pessoa.models import Pessoa
from material.models import MaterialAdaptado
from django.utils import timezone
from datetime import datetime
import os


# Create your models here.

def get_revista_upload_path(instance, filename):
    date_part = datetime.now().strftime('%Y/%m')

    if isinstance(instance, MaterialAdaptado):
        return os.path.join('materiais',instance.tipo, date_part,filename)
    return os.path.join('revista', date_part, filename)


class Solicitante(models.Model):
    data_registro = models.DateTimeField(auto_now_add=True)
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.pessoa.__str__()

class Revista(models.Model):    
    titulo = models.CharField(max_length = 255)
    data_registro = models.DateTimeField(auto_now_add=True, verbose_name='Data de registro')
    is_disponivel_para_assinatura = models.BooleanField(default=False, verbose_name="Disponível para assinatura?")

    def __str__(self) -> str:
        return self.titulo

class Assinatura(models.Model):
    ESTADO_CHOICES =[
        ('vigente','vigente'),
        ('cancelado','cancelado'),
    ]
    estado = models.CharField(max_length=255,choices=ESTADO_CHOICES, default='vigente')
    revista = models.ForeignKey(
        Revista,
        on_delete= models.CASCADE,
        limit_choices_to={'is_disponivel_para_assinatura':True},
        null = True, blank= True
        )
    data_registro = models.DateTimeField(auto_now_add=True, verbose_name='Data de registro')
    data_ultima_alteracao = models.DateTimeField(null=True)
    observacao = models.CharField(max_length=255, verbose_name='Observação', blank=True)
    solicitante = models.ForeignKey(Solicitante, on_delete=models.CASCADE, verbose_name='Solicitante / Assinante')

    def __str__(self) -> str:
        return f'{self.revista}, solicitante: {self.solicitante}'
    
    def get_admin_url(self):
        return '/admin/assinatura/assinatura/{0}/change'.format(self.id)

    def save(self, *args, **kwargs):
        if self.pk:
            self.data_ultima_alteracao = timezone.now()
            # if self.your_field == 'some_value':
            #     self.other_field = 'updated_value'
        
        super().save(*args, **kwargs)
    
class Assinante(models.Model):
    nome = models.CharField(max_length=255, verbose_name="nome da pessoa que receberá a revista")
    assinatura = models.OneToOneField(Assinatura, on_delete=models.CASCADE)


class RegistroEnvioAssinaturas(models.Model):    
    class Meta:
        verbose_name_plural = 'Configurar envio de Assinaturas'
    nome = models.CharField(max_length=255, verbose_name='Nome', blank=False)
    enviado = models.BooleanField(default=False, verbose_name='Enviado?')
    remetente = models.CharField(max_length=255, verbose_name='Remetente',default='Instituto Benjamin Constant', blank=True)
    identificacao = models.CharField(max_length=255, verbose_name='Identificação',default='Cecograma', blank=True)
    data_registro = models.DateTimeField(verbose_name='Data de registro', auto_now_add=True)
    observacao = models.CharField(max_length=255, verbose_name='Observação', blank=True)

    def __str__(self) -> str:
        return self.nome

class TipoRemessa(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Remessa(models.Model):    
    class Meta:
        verbose_name = 'Remessa'
        verbose_name_plural = 'Remessas para Envio (das edições das revistas)'
    registro_envio = models.ForeignKey(RegistroEnvioAssinaturas, on_delete= models.CASCADE, null = True, blank= True)
    tipo_remessa = models.ManyToManyField('TipoRemessa',max_length=255)
    data_registro = models.DateTimeField(verbose_name='Data de registro', auto_now_add=True)
    data_envio = models.DateField(null=True,blank=True)
    quantidade = models.PositiveIntegerField(null=True, blank=True)
    observacao = models.CharField(max_length=255, verbose_name='Observação', blank=True)
    ordem = models.CharField(max_length=255, verbose_name='ordem', blank=True)

    def __str__(self):        
        tipo_remessas = [str(tipo_remessa) for tipo_remessa in self.tipo_remessa.all()]        
        tipo_remessa = " e ".join(tipo_remessas)
        return tipo_remessa + ' ' + self.ordem


class EdicaoRevistaAssinatura(models.Model):
    class Meta:
        verbose_name = 'Edição da Revista'
        verbose_name_plural = 'Edições das Revistas (que serão enviadas)'

    revista = models.ForeignKey(
        Revista, 
        on_delete= models.CASCADE,
        limit_choices_to={'is_disponivel_para_assinatura':True},
        null = True, blank= True
        )
    assinaturas = models.ManyToManyField(
        Assinatura,
        limit_choices_to={'estado':'vigente'}        
        )
    edicao = models.CharField(max_length = 255, null=True, blank=True)                
    quantidade_paginas = models.PositiveIntegerField(null=True, blank=True, default=0)
    peso = models.PositiveIntegerField(null=True, blank=True, verbose_name='peso em gramas', default=0)
    registro_envio = models.ForeignKey(RegistroEnvioAssinaturas, on_delete= models.CASCADE, null = True, blank= True)
    arquivo_original = models.FileField(upload_to=get_revista_upload_path, null = True, blank= True)
    quantidade_assinaturas_RJ = models.PositiveIntegerField(null=True,verbose_name='Qtd. ass. Rio de Janeiro (ativas)', blank=True, default=0)
    quantidade_assinaturas_Es = models.PositiveIntegerField(null=True,verbose_name='Qtd. ass. Estrangeiros (ativas)', blank=True, default=0)
    quantidade_assinaturas_OE = models.PositiveIntegerField(null=True,verbose_name='Qtd. ass. Outros Estados (ativas)', blank=True, default=0)

    def __str__(self) -> str:
        return '{0}. Edição: {1}'.format(self.revista, self.edicao)
    