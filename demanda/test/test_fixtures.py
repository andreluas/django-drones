from django.test import TestCase
from demanda.models import *

class FixtureDataTestCase(TestCase):

    fixtures = ['seeding']

    def test_verifica_carregamento_da_fixture(self):
        fixture = Uf.objects.get(pk=1)
        ufs = Uf.objects.all()
        cidades = Cidade.objects.all()
        self.assertEqual(fixture.uf, 'RJ')
        self.assertEqual(len(ufs), 3)
        self.assertEqual(len(cidades), 3)
