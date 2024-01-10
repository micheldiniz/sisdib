from django.db import models

# Create your models here.

class Material(models.Model):
    pass

class MaterialBraille(Material, models.Model):
    pass

class MaterialAmpliado(Material, models.Model):
    pass