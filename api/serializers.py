from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import Fornecedor, RegistosRespostas, TipoRegistos, Registos,QuestoesRegistos


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
        fields = ['id', 'registo', 'questao', 'resposta']


class RecordSerializer(ModelSerializer):
    class Meta:
        model = Registos
        fields = ['id', 'dataregisto', 'tiporegisto', 'status']

class RecordQuestionsSerializer(ModelSerializer):
    class Meta:
        model = QuestoesRegistos
        fields = ['id', 'tipoderegisto', 'questao']