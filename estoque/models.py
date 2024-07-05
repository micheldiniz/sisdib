from django.db import models
from material.models import MaterialAdaptado


# Create your models here.
class EntradaEstoque(models.Model):
    material = models.OneToOneField(MaterialAdaptado,limit_choices_to={'tipo':'braille'}, on_delete=models.CASCADE)
    quantidade_impressa = models.PositiveBigIntegerField(null=False, blank=False, default=0)
    data_registro = models.DateField(verbose_name='Data da impressão')

    def __str__(self) -> str:
        return f"{self.material}, impressões: {self.quantidade_impressa}"