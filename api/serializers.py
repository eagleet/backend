from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import Fornecedor


class FornecedorSerializer(ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = ['id', 'nome', 'nif', 'morada', 'email', 'telefone']