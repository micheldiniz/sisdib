from django.core.management.base import BaseCommand, CommandError
from cliente.models import Solicitante, Assinatura
import csv, datetime, re, random
from material.models import MaterialAdaptado

class Command(BaseCommand):
    help = 'Importa dados para pessoa física (CPF é definido como valor único, porém null é aceito)'

    # def add_arguments(seld):
    #     pass


    def handle(self, *args, **options):

        superbraille = MaterialAdaptado.objects.filter(material__titulo='Superbraille').first()
        pontinhos = MaterialAdaptado.objects.filter(material__titulo='Pontinhos').first()
        rbc = MaterialAdaptado.objects.filter(material__titulo='Revista Brasileira para Cegos').first()
  
        solicitantes = Solicitante.objects.all()
        if (superbraille and pontinhos and rbc):
            for solicitante in solicitantes:
                number = random.choice([1,2,3])
                if number==1:
                    Assinatura.objects.create(solicitante = solicitante, material = pontinhos)
                    Assinatura.objects.create(solicitante = solicitante, material = superbraille)
                if number == 2:
                    Assinatura.objects.create(solicitante = solicitante, material = rbc)
                if number == 3:
                    Assinatura.objects.create(solicitante = solicitante, material = pontinhos)
                    Assinatura.objects.create(solicitante = solicitante, material = superbraille)
                    Assinatura.objects.create(solicitante = solicitante, material = rbc)
            self.stdout.write(self.style.SUCCESS('Successfully created Assinatura objects'))
        # self.stdout.write(self.style.SUCCESS('no record found'))
        