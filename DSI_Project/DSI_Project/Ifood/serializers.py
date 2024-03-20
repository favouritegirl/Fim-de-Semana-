from rest_framework import serializers
from .models import consumidor, Endereco, Email

class ConsumidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = consumidor
        fields = ['id', 'name', 'email', 'password,' 'telefone', 'cpf']


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id', 'cep', 'id_consumidor']

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model: Email
        fields = ['assunto', 'mensagem', 'remetente', 'destinatarios' ]