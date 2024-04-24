from django.db import models
from cliente.models import Solicitante
from material.models import MaterialAdaptado

# Create your models here.

class RegistroEnvioPedidos(models.Model):
    ESTADO_CHOICES = [
        ('novo','novo'),
        ('processado','processado'),
        ('enviado','enviado'),
        ('finalizado','finalizado'),
        ('pendente','pendente'),
    ]
    class Meta:
        verbose_name_plural = 'Registo de envio de Pedidos'
    estado_envio = models.CharField(max_length=255, choices = ESTADO_CHOICES, default = "novo")    
    descricao = models.CharField(max_length=255, verbose_name='Descrição', blank=True)
    data_registro = models.DateTimeField(verbose_name='Data de registro', auto_now_add=True)
    data_envio = models.DateField(null=True,blank=True)
    observacao = models.CharField(max_length=255, verbose_name='Observação', blank=True)
    
    def __str__(self) -> str:
        return f'{self.descricao}(envio: {self.data_envio})'

class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('novo','novo'),
        ('processado','processado'),
        ('enviado','enviado'),
        ('finalizado','finalizado'),
        ('pendente','pendente'),
    ]
    data_registro = models.DateTimeField(auto_now_add=True)
    numero_pedido = models.PositiveBigIntegerField()
    estado_do_pedido = models.CharField(max_length=255, choices = ESTADO_CHOICES, default = "novo")
    solicitante = models.ForeignKey(Solicitante,on_delete=models.CASCADE)
    observacao = models.CharField(max_length=255, null=True, blank=True)
    registro_envio = models.ForeignKey(
        RegistroEnvioPedidos,
        # limit_choices_to={'estado_do_pedido':'novo'},
        on_delete=models.CASCADE,
        null=True,
        blank = True
        )

    def __str__(self):        
        return self.numero_pedido.__str__()
    
    def get_admin_url(self):
        return f'/admin/pedido/pedido/{self.id}/change/'

class ItemPedido(models.Model):
    ESTADO_CHOICES = [
        ("aceito","aceito"),
        ("indisponivel","indisponivel"),
        ("pendente","pendente"),
    ]
    quantidade = models.PositiveIntegerField()
    
    material = models.ForeignKey(
        MaterialAdaptado, 
        on_delete=models.CASCADE,
        # limit_choices_to={'is_disponivel_para_pedido': True}
        )
   
    estado = models.CharField(max_length=255, choices=ESTADO_CHOICES)
    observacao = models.CharField(max_length=255, null=True, blank=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens_pedido')    
   
    def __str__(self):          
        return f"{self.material} quantidade: {self.quantidade}"


