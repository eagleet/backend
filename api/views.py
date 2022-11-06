# from multiprocessing import context
# from re import search
# from warnings import filters
from django.shortcuts import render
# from django.http import response
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Fornecedor
from .serializers import FornecedorSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import filters

# from api import serializers
# from rest_framework.serializers import Serializer

# Create your views here.

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/suppliers/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of suppliers'
        },
        {
            'Endpoint': '/suppliers/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single supplier object'
        },
        {
            'Endpoint': '/suppliers/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new supplier with data sent in post request'
        },
        {
            'Endpoint': '/suppliers/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing supplier with data sent in post request'
        },
        {
            'Endpoint': '/supplier/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)


# @api_view(['GET', 'POST'])
# def getSupplier(request):

#     if request.method == 'GET':
#         return getSupplierList(request)

#     if request.method == 'POST':
#         return createSupplier(request)


# @api_view(['GET', 'PUT', 'DELETE'])
# def getSupplier(request, pk):

#     if request.method == 'GET':
#         return getNoteDetail(request, pk)

#     if request.method == 'PUT':
#         return updateNote(request, pk)

#     if request.method == 'DELETE':
#         return deleteNote(request, pk)




# class SupplierFiniteView(ListCreateAPIView):
#     serializer_class = FornecedorSerializer
#     filter_backends=[DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

#     filterset_fields = ['id', 'nome', 'nif', 'morada', 'email', 'telefone']
#     search_fields = ['id', 'nome', 'nif', 'morada', 'email', 'telefone']
#     ordering_fields = ['id', 'nome', 'nif', 'morada', 'email', 'telefone']

    
#     def perform_create(self, serializer):
#         return serializer.save(user=self.request.user)

#     def get_queryset(self):
#         return Fornecedor.objects.filter(user=self.request.user)

# class SupplierDetailAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class = FornecedorSerializer
#     lookup_field = "id"

#     def get_queryset(self):
#         return Fornecedor.objects.filter(owner=self.request.user)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token
    

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]

    return Response(routes)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getSuppliers(request):
    user = request.user
    suppliers = Fornecedor.objects.all()
    serializer = FornecedorSerializer(suppliers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getSupplier(request, pk):
    suppliers = Fornecedor.objects.get(id=pk)
    serializer = FornecedorSerializer(suppliers, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createSupplier(request): 
    serializer = FornecedorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateSupplier(request, pk):
    data = request.data
    fornecedor = Fornecedor.objects.get(id=pk)
    serializer = FornecedorSerializer(instance=fornecedor, data=data)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

