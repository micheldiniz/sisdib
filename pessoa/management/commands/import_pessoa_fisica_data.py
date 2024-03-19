from django.core.management.base import BaseCommand, CommandError
from pessoa.models import PessoaFisica, Endereco, Contato
from cliente.models import Cliente
import csv, datetime, re

class Command(BaseCommand):
    help = 'Importa dados para pessoa física (CPF é definido como valor único, porém null é aceito)'

    # def add_arguments(seld):
    #     pass


    def handle(self, *args, **options):
        #clear all data
        PessoaFisica.objects.all().delete()


        # Your data import logic here
        csv_validate = open('pessoa/management/data/data_validate.csv', 'w')


        with open('pessoa/management/data/data.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            # date = datetime.datetime.now()
            for row in reader:    
                if(row['pessoa_fisica']=='TRUE' and row['instituicao']=='FALSE' or row['cpf'] and (row['tipo_instituicao'] == "Pessoa Física" or row['tipo_instituicao'] == "Estrangeiros") ):
                    pessoa_fisica = Command.toPessoaFisica(row)
                    endereco = Command.toEndereco(row, pessoa_fisica)
                    contato = Command.toContato(row, pessoa_fisica)
                    cliente = Cliente.objects.create(
                        pessoa = pessoa_fisica
                    )
                    break
                else:
                    csv_validate.write(str(row) + '\n')
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))

    @staticmethod
    def toPessoaFisica(row) -> PessoaFisica:

        pessoa_fisica = PessoaFisica.objects.create(
            cpf = row['cpf'],
            nome = row['solicitante'].upper(),
            is_estrangeiro = False,
            nacionalidade = 'Brasileiro'
        )
        
        # pessoa_fisica.is_estrangeiro = False

        if(len(row['solicitante'])==0):
            pessoa_fisica.nome = row['nome'].upper()        

        data_registro = row['data_registro']
        if data_registro:
            pessoa_fisica.data_registro = Command.format_date(data_registro)

        data_nascimento = row['data_nascimento']
        if data_nascimento:
            pessoa_fisica.data_nascimento = Command.format_date(data_nascimento)

        if (row['tipo_instituicao'] == 'Estrangeiros'):
            pessoa_fisica.is_estrangeiro = True
            pessoa_fisica.nacionalidade = row['uf']

        pessoa_fisica.save()   
                    
        return pessoa_fisica

    @staticmethod
    def toEndereco(row, pessoa) -> Endereco: 
            
        endereco = Endereco.objects.create(
            pessoa = pessoa,
            cep = row['cep'],         
            logradouro = row['endereco'],
            numero = row['numero'],
            complemento = row['complemento'],
            bairro = row['bairro'],
            cidade = row['cidade'],
            estado = row['uf'],
        )
        
        endereco.pais = 'Brasil'
        
        if (row['tipo_instituicao'] == 'Estrangeiros'):
            endereco.pais = row['uf']
        
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
        
        if (len(row['contato_fone'])>1):
            contato.telefone = row['ddd'] + ' ' + row['contato_fone']

        return contato

    @staticmethod
    def validate_date(date_str):
        """
        Validates a date string in the format YYYY-MM-DD, considering leap years.

        Args:
            date_str (str): The date string to validate.

        Returns:
            bool: True if the date is valid, False otherwise.
        """

        regex = r"^(\d{4})-(\d{2})-(\d{2})$"
        match = re.match(regex, date_str)

        if not match:
            return False

        year, month, day = match.groups()

        try:
            year = int(year)
            month = int(month)
            day = int(day)
        except ValueError:
            return False

        # Check month and day validity
        if month < 1 or month > 12:
            return False
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            days_in_month[1] = 29  # Leap year
        if day < 1 or day > days_in_month[month - 1]:
            return False

        return True
    
    @staticmethod
    def format_date(date_str:str) -> datetime.date:        

        if (Command.validate_date(date_str)):
            return datetime.strptime(date_str, "%Y-%m-%d")
               
        try:
            date_parts = [int(part) for part in re.split(r"[/\-_]", date_str)]
        except (ValueError, IndexError):
            raise ValueError("Invalid date format. Please use DD/MM/YYYY, MM-DD-YYYY, or similar.")

        day, month, year = date_parts

        try:
            datetime.datetime(year, month, day)
        except ValueError:
            raise ValueError("Invalid date value. Please provide a valid date within the calendar range.")

        formatted_date = datetime.datetime(year, month, day).strftime("%Y-%m-%d")

        print(formatted_date)  # Output: 1990-06-26
        
        return formatted_date


    