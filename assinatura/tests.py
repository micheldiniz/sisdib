from django.test import TestCase
from assinatura.models import Assinatura, Solicitante
from pessoa.models import PessoaFisica
# Create your tests here.

class PessoaFisicaTestCase():
    def setUp(self):
        assinatura = Assinatura.objects.create(estado=0)
        solicitante = Solicitante.objects.create(assinatura)
        PessoaFisica.objects.create(nome="João Ricardo")
        pass
    
    def test_pessoa_fisica_has_solicitante(self):
        pessoa_fisica = PessoaFisica.objects.get(nome="João Ricardo")
        
        self.assertIs(pessoa_fisica.nome, True)


