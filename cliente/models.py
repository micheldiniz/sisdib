from django.db import models
from pessoa.models import Pessoa
from material.models import MaterialAdaptado
from django.utils import timezone

# Create your models here.
class Cliente(models.Model):
    data_registro = models.DateTimeField(auto_now_add=True)
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.pessoa.__str__()

class Assinatura(models.Model):
    ESTADO_CHOICES =[
        ('1','vigente'),
        ('0','cancelado'),
    ]
    estado = models.CharField(max_length=2,choices=ESTADO_CHOICES, default='vigente')
    material = models.ForeignKey(
        MaterialAdaptado, 
        on_delete= models.CASCADE,
        limit_choices_to={'is_disponivel_para_assinatura':True})    
    data_registro = models.DateTimeField(auto_now_add=True, verbose_name='Data de registro')
    data_ultima_alteracao = models.DateTimeField(null=True)
    observacao = models.CharField(max_length=255, verbose_name='Observação', blank=True)
    solicitante = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.material}, solicitante: {self.solicitante}'
    
    def save(self, *args, **kwargs):
        if self.pk:
            self.data_ultima_alteracao = timezone.now()
            # if self.your_field == 'some_value':
            #     self.other_field = 'updated_value'
        
        super().save(*args, **kwargs)
    
class Assinante(models.Model):
    nome = models.CharField(max_length=255, verbose_name="nome da pessoa que receberá o material")
    assinatura = models.OneToOneField(Assinatura, on_delete=models.CASCADE)
