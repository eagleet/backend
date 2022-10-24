from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Fornecedor
from .serializers import FornecedorSerializer

# Create your views here.

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/supplier/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/supplier/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/supplier/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/supplier/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/supplir/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getSuppliers(request):
    suppliers = Fornecedor.objects.all()
    serializer = FornecedorSerializer(suppliers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSupplier(request, pk):
    suppliers = Fornecedor.objects.get(id=pk)
    serializer = FornecedorSerializer(suppliers, many=False)
    return Response(serializer.data)