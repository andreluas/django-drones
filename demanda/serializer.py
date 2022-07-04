from rest_framework import serializers
from demanda.models import Demanda
from demanda.validators import contato_valido
from django.contrib.auth.models import User
    
class DemandaSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Demanda
        fields = '__all__'
    def validate(self, data):
        if not contato_valido(data['info_contato']):
            raise serializers.ValidationError({'info_contato': 'Celular de contato deve seguir o padrão: 21 99999-9999'})
        return data

class UserSerializer(serializers.ModelSerializer):
    demandas = serializers.PrimaryKeyRelatedField(many=True, queryset=Demanda.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'demandas']