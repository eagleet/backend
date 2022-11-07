from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import Fornecedor, RegistosRespostas


class FornecedorSerializer(ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = ['id', 'nome', 'nif', 'morada', 'email', 'telefone']

class RecordSerializer(ModelSerializer):
    class Meta:
        model = RegistosRespostas
        fields = ['registo', 'questao', 'resposta']