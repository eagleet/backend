# from multiprocessing import context
# from re import search
# from warnings import filters
from django.shortcuts import render
# from django.http import response
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import RegistosRespostas, Fornecedor, TipoRegistos,Registos, QuestoesRegistos
from .serializers import RecordQuestionsSerializer, RecordSerializer, FornecedorSerializer, RecordTypeSerializer, RecordResponsesSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import filters

# from api import serializers
# from rest_framework.serializers import Serializer

# Create your views here.

#############################
#  ROUTES  #
#############################

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
            'description': 'Deletes and exiting supplier'
        },
                {
            'Endpoint': '/api/token',
            'method': 'POST',
            'body': None,
            'description': 'Returns Refresh and Access Token'
        },
                {
            'Endpoint': '/api/token/refresh',
            'method': 'POST',
            'body': None,
            'description': 'Returns a new Access Token'
        },
    ]
    return Response(routes)

#############################
#  AUTHENTICATION  #
#############################

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

#############################
#  SUPPLIERS  #
#############################

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

#############################
#  REGISTOS  #
#############################

@api_view(['GET'])
def getRecords(request):
    respostasregistos = RegistosRespostas.objects.all()
    registos = Registos.objects.all()
    registos1 = RecordSerializer(registos, many=True)
    return Response(registos1.data)

@api_view(['GET'])
def getRecord(request, pk):
    registosportipo = Registos.objects.filter(tiporegisto=pk)
    registosSerializer = RecordSerializer(registosportipo, many=True)
    return Response(registosSerializer.data)

@api_view(['POST'])
def createRecord(request): 
    serializer = RecordResponsesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateRecord(request, pk):
    data = request.data
    registo = RegistosRespostas.objects.get(id=pk)
    serializer = RecordResponsesSerializer(instance=registo, data=data)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# Cria novo registo #

@api_view(['POST'])
def createRegisto(request): 
    serializer = RecordSerializer(data=request.data)
    #questoes = QuestoesRegistos.objects.filter(tipoderegisto=request.data.get('tiporegisto'))
    #print(questoes)
    if serializer.is_valid():
        #perguntas = questoes.count()
        #respostas = RegistosRespostas.objects.bulk_create(questoes,perguntas)
        serializer.save()
    return Response(serializer.data)

# GET Tiposderegisto #

@api_view(['GET'])
def getTipo(request):
    tiposderegisto = TipoRegistos.objects.all()
    serializer = RecordTypeSerializer(tiposderegisto, many=True)
    return Response(serializer.data)

# GET Tiposderegisto.questoes #

@api_view(['GET'])
def getQuestoes(request, pk):
    respostasregistos = QuestoesRegistos.objects.filter(tipoderegisto__pk=pk)
    serializer = RecordQuestionsSerializer(respostasregistos, many=True)
    return Response(serializer.data)

#############################
#  NOTES  #
#############################

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