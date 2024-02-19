from django.core.management.base import BaseCommand, CommandError
from pessoa.models import PessoaFisica, Endereco, Contato
from cliente.models import Cliente
import csv, datetime

class Command(BaseCommand):
    help = 'Importa dados para pessoa física (CPF é definido como valor único, porém null é aceito)'

    # def add_arguments(seld):
    #     pass


    def handle(self, *args, **options):
        # Your data import logic here
        with open('pessoa/management/data/pessoa_fisica.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            date = datetime.datetime.now()
            for row in reader:
                if(len(row['data_registro']) > 1):
                    date = datetime.datetime.strptime(row['data_registro'],"%d/%m/%Y").strftime("%Y-%m-%d")

                pessoa = PessoaFisica.objects.create(
                    nome=row['nome'],
                    data_registro=date
                    # data=row['field2'],
                    # Map CSV fields to model fields
                )
                
                # Create Endereco
                endereco = Endereco.objects.create(
                    pessoa=pessoa,  # OneToOne relationship
                    # logradouro=row['logradouro'],
                    # other fields
                )

                # Create Contato
                contato = Contato.objects.create(
                    pessoa=pessoa,  # OneToOne relationship
                    # telefone=row['telefone'],
                    # other fields
                )

                cliente = Cliente.objects.create(
                    pessoa = pessoa
                )



        self.stdout.write(self.style.SUCCESS('Data imported successfully'))