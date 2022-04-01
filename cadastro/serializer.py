from rest_framework import serializers
from cadastro.models import Cliente
from cadastro.validators import *
from rest_framework import serializers

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__' #'['id', 'nome', 'email', 'telefone', 'endereço_completo', 'profissao', 'curriculo_upload']'
    def validate(self, data):
        if not telefone_valido(data['telefone']):
            raise serializers.ValidationError({'telefone':"Apenas a inclusão de números é permitido neste campo"})
        return data
        