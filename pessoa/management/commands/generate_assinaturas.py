from django.core.management.base import BaseCommand, CommandError
from assinatura.models import Solicitante, Assinatura
import csv, datetime, re, random
from assinatura.models import Revista

class Command(BaseCommand):
    help = 'Importa dados para pessoa física (CPF é definido como valor único, porém null é aceito)'

    # def add_arguments(seld):
    #     pass


    def handle(self, *args, **options):

        superbraille = Revista.objects.filter(material__titulo='Superbraille').first()
        pontinhos = Revista.objects.filter(material__titulo='Pontinhos').first()
        rbc = Revista.objects.filter(material__titulo='Revista Brasileira para Cegos').first()
  
        solicitantes = Solicitante.objects.all()
        if (superbraille and pontinhos and rbc):
            for solicitante in solicitantes:
                number = random.choice([1,2,3])
                if number==1:
                    Assinatura.objects.create(solicitante = solicitante, revista = pontinhos)
                    Assinatura.objects.create(solicitante = solicitante, revista = superbraille)
                if number == 2:
                    Assinatura.objects.create(solicitante = solicitante, revista = rbc)
                if number == 3:
                    Assinatura.objects.create(solicitante = solicitante, revista = pontinhos)
                    Assinatura.objects.create(solicitante = solicitante, revista = superbraille)
                    Assinatura.objects.create(solicitante = solicitante, revista = rbc)
            self.stdout.write(self.style.SUCCESS('Successfully created Assinatura objects'))
        # self.stdout.write(self.style.SUCCESS('no record found'))
        