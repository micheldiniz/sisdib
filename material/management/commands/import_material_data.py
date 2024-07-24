from django.core.management.base import BaseCommand, CommandError
from material.models import Material, MaterialAdaptado, Classificacao
import csv, datetime, re

class Command(BaseCommand):
    help = 'Importa dados de material braille'

    
    def handle(self, *args, **options):
        #clear all data
        MaterialAdaptado.objects.all().delete()
        Material.objects.all().delete()

        with open('material/management/data/data_materiais_braille.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                material = Material.objects.create(
                    classificacao = Classificacao.objects.get(id=row['classificacao']),                    
                    titulo = row['titulo'],
                    autor = row['autor'],
                    ano_publicacao = row['ano_publicacao']
                )
                material_adaptado = MaterialAdaptado.objects.create(
                    material = material,
                    tipo = 'braille',
                    quantidade_paginas = row['paginas_braille'],
                    is_disponivel_para_pedido = True
                )
                
              
            self.stdout.write(self.style.SUCCESS('Data imported successfully'))
