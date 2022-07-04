from rest_framework import viewsets
from endereco.models import Uf, Cidade
from endereco.serializer import CidadeSerializer, UfSerializer

class UfViewSet(viewsets.ModelViewSet):
    queryset = Uf.objects.all()
    serializer_class = UfSerializer
    http_method_names = ['get']

class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    http_method_names = ['get']