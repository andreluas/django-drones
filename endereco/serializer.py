from rest_framework import serializers
from endereco.models import Uf, Cidade

class UfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uf
        fields = '__all__'

class CidadeSerializer(serializers.ModelSerializer):
    uf = serializers.ReadOnlyField(source='uf.uf')
    class Meta:
        model = Cidade
        fields = '__all__'