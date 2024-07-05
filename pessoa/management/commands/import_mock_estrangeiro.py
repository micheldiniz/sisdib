from django.core.management.base import BaseCommand, CommandError
from pessoa.models import PessoaFisica, Endereco, Contato
from assinatura.models import Solicitante
import csv, datetime, re, random

class Command(BaseCommand):
    help = 'Importa dados para pessoa física (CPF é definido como valor único, porém null é aceito)'

    # def add_arguments(seld):
    #     pass


    def handle(self, *args, **options):
        #clear all data
        # PessoaFisica.objects.all().delete()

        with open('pessoa/management/data/mock_data.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)            
            for row in reader:    
                    pessoa_fisica = Command.toPessoaFisica(row)
                    endereco = Command.toEndereco(row, pessoa_fisica)
                    contato = Command.toContato(row, pessoa_fisica)
                    cliente = Solicitante.objects.create(
                        pessoa = pessoa_fisica
                    )
                    cliente.save()
                
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))

    @staticmethod
    def toPessoaFisica(row) -> PessoaFisica:

        pessoa_fisica = PessoaFisica.objects.create(
            cpf = row['cpf'],
            nome = row['nome'].upper(),
            is_estrangeiro = True,
            nacionalidade = row['nacionalidade'],
            data_registro = row['data_registro'],       
            data_nascimento = row['data_nascimento'],
        )
        pessoa_fisica.save()   
        return pessoa_fisica

    @staticmethod
    def toEndereco(row, pessoa) -> Endereco: 
            
        endereco = Endereco.objects.create(
            pessoa = pessoa,
            cep = row['cep'],         
            logradouro = row['logradouro'] + ' ' + row['rua'],
            numero = random.randint(1,1000),            
            bairro = row['bairro'],
            cidade = row['cidade'],
            estado = row['estado'],
            pais = row['pais'],
        )
                
        endereco.save()
        return endereco
    
    @staticmethod
    def toContato(row, pessoa) -> Contato:
        contato = Contato.objects.create(
            pessoa = pessoa,
            celular = row['celular'],
            email = row['email'],
            nome_contato = row['nome_contato']
        )

        return contato