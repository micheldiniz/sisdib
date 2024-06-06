from django.test import TestCase
from assinatura.models import *
# Create your tests here.

class PessoaFisicaTestCase():
    def setUp(self):
        assinatura = Assinatura.objects.create(estado=0)
        cliente = Cliente.objects.create(assinatura)
        PessoaFisica.objects.create(nome="João Ricardo")
    
    def test_pessoa_fisica_has_cliente(self):
        pessoa_fisica = PessoaFisica.objects.get(nome="João Ricardo")
        
        self.assertIs(pessoa_fisica.nome, True)

