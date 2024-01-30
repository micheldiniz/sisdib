from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from cliente.models import Cliente

# Create your models here.

class Pedido(models.Model):        
    data_registro = models.DateTimeField(auto_now_add=True)
    numero_pedido = models.PositiveBigIntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):        
        return self.numero_pedido.__str__()

class ItemPedido(models.Model):
    ESTADO_CHOICES = {
        "aceito":"aceito",
        "indisponivel":"indisponivel",
        "pendente":"pendente",
    }
    quantidade = models.PositiveIntegerField()
    material_object_id = models.IntegerField()
    material_content_type = models.ForeignKey(
        ContentType,
        on_delete = models.PROTECT,
    )
    material = GenericForeignKey(
        'material_content_type',
        'material_object_id',
    )
    estado = models.CharField(max_length=255, choices=ESTADO_CHOICES)
    observacao = models.CharField(max_length=255)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)    

    def getGenericObject(self):
        content_type = ContentType.model_class(self.material_content_type)
        obj = content_type.objects.get(id=self.material_object_id)
        return obj

    def __str__(self):  
        obj =  self.getGenericObject() 
        return f"{obj.__str__()} quantidade: {self.quantidade}"
