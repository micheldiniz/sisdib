from django.core.management.base import BaseCommand, CommandError
from cliente.models import Solicitante, Assinatura
import csv, datetime, re, random
from material.models import MaterialAdaptado

class Command(BaseCommand):
    help = 'Importa dados para pessoa física (CPF é definido como valor único, porém null é aceito)'

    # def add_arguments(seld):
    #     pass


    def handle(self, *args, **options):

        superbraille = MaterialAdaptado.objects.get(pk=3)
        pontinhos = MaterialAdaptado.objects.get(pk=6)
        rbc = MaterialAdaptado.objects.get(pk=5)

        solicitantes = Solicitante.objects.all()

        for solicitante in solicitantes:
            number = random.choice([1,2,3])
            if number==1:
                Assinatura.objects.create(solicitante = solicitante,material = MaterialAdaptado.objects.get(pk=3))
                Assinatura.objects.create(solicitante = solicitante,material = MaterialAdaptado.objects.get(pk=6))
            if number == 2:
                Assinatura.objects.create(solicitante = solicitante,material = MaterialAdaptado.objects.get(pk=5))
            if number == 3:
                Assinatura.objects.create(solicitante = solicitante,material = MaterialAdaptado.objects.get(pk=3))
                Assinatura.objects.create(solicitante = solicitante,material = MaterialAdaptado.objects.get(pk=6))
                Assinatura.objects.create(solicitante = solicitante,material = MaterialAdaptado.objects.get(pk=5))
        self.stdout.write(self.style.SUCCESS('Successfully created Assinatura objects'))