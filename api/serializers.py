from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import Fornecedor, RegistosRespostas, TipoRegistos, Registos


class FornecedorSerializer(ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = ['id', 'nome', 'nif', 'morada', 'email', 'telefone']

class RecordTypeSerializer(ModelSerializer):
    class Meta:
        model = TipoRegistos
        fields = [ 'id','name', 'periocidade',]

class RecordResponsesSerializer(ModelSerializer):
    class Meta:
        model = RegistosRespostas
        fields = ['registo', 'questao', 'resposta']


class RecordSerializer(ModelSerializer):
    class Meta:
        model = Registos
        fields = ['dataregisto', 'tiporegisto']