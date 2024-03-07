from rest_framework import serializers
from .models import consumidor, Endereco

class ConsumidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = consumidor
        fields = ['id', 'name', 'email', 'password']


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id', 'cep', 'id_consumidor']