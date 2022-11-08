from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

#############################
#  SUPPLIERS  #
#############################      

class Fornecedor(models.Model):

    nome = models.CharField(max_length=100, null=True)
    nif = models.CharField(max_length=11, null=True)
    morada = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    telefone = models.IntegerField(null=True)

    def __str__(self):
        return self.nome

    class Meta: verbose_name_plural = "Fornecedores"


class FornecedorContactos(models.Model):

    fornecedor = models.ForeignKey(Fornecedor, null=True, on_delete=models.SET_NULL)
    departamento = models.CharField(max_length=11, null=True)
    email = models.EmailField(max_length=254, null=True)
    telefone = models.IntegerField(null=True)

    def __str__(self):
        return self.fornecedor.nome

    class Meta: verbose_name_plural = "Contactos Fornecedores"


class MP(models.Model):
    nome = models.CharField(max_length=100, null=True)

    class Meta: verbose_name_plural = "MP"

    def __str__(self):
        return self.nome


class Alergeneo(models.Model):
    nome = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=500, null=True)
    abreviatura = models.CharField(max_length=50, null=True)

    class Meta: verbose_name_plural = "Alergéneos"

    def __str__(self):
        return self.nome


class MateriaPrima(models.Model):
    TIPODEPRODUTO = (
                ('Simples', 'Simples'),
                ('Composto', 'Composto'),
                ('Intermédio', 'Intermédio'),
                )
    
    mp = models.ForeignKey(MP, null=True, on_delete=models.SET_NULL)
    nomecomercial = models.CharField(max_length=100, null=True)
    codigo = models.CharField(max_length=100, null=True)
    tipodeproduto = models.CharField(max_length=100, null=True, choices=TIPODEPRODUTO)
    descrição = models.CharField(max_length=200, null=True)
    fornecedor = models.ForeignKey(Fornecedor, null=True, on_delete=models.SET_NULL)
    ingredientes = models.CharField(max_length=500, null=True)
    contemalergeneo = models.ManyToManyField(Alergeneo, related_name="bar")
    podeconteralergeneo = models.ManyToManyField(Alergeneo, related_name="baz")
    proteinas = models.FloatField(null=True)
    gordura = models.FloatField(null=True)
    gordurassaturadas = models.FloatField(null=True)
    hidratosdecarbono = models.FloatField(null=True)
    acucares = models.FloatField(null=True)
    minerais = models.FloatField(null=True)
    fibra = models.FloatField(null=True)
    humidade = models.FloatField(null=True)
    namg = models.FloatField(null=True)
    kjoule = models.FloatField(null=True)
    kcal = models.FloatField(null=True)
    criado = models.DateField(auto_now_add=True, null=True)
    lastupdate = models.DateField(auto_now=True, null=True)

    class Meta: verbose_name_plural = "Matérias Primas"

    def __str__(self):
        return self.nomecomercial
        
class Receita(models.Model):
    nome = models.CharField(max_length=100, null=True)
    
    class Meta: verbose_name_plural = "Receitas"

    def __str__(self):
        return self.nome

class IngredientesReceita(models.Model):
    mp = models.ForeignKey(MateriaPrima, db_column='mp', null=True, on_delete=models.SET_NULL)
    receita = models.ForeignKey(Receita, db_column='_id', null=True, on_delete=models.SET_NULL)
    quantidade = models.FloatField(null=True)

    class Meta: verbose_name_plural = "Receitas (Ingredientes)"

    def __str__(self):
        return self.receita.nome

class Produto(models.Model):
    nome = models.CharField(max_length=500, null=True)
    receitas = models.ManyToManyField(Receita)
    peso = models.IntegerField(null=True)

    class Meta: verbose_name_plural = "Produtos"

    def __str__(self):
        return self.nome

class Lote(models.Model):
    produto = models.ManyToManyField(Produto)
    datadeproducao = models.DateField(auto_now_add=True, null=True)

    lote = models.CharField(max_length=50, null=True)

    class Meta: verbose_name_plural = "Lotes"
    
    def __str__(self):
        return self.lote

#############################
#  RECORDS  #
#############################    

class TipoRegistos(models.Model):
    name = models.CharField(max_length=100, null=True)
    periocidade = models.IntegerField(null=True)

    class Meta: verbose_name_plural = "Tipo de Registo"

    def __str__(self):
        return self.name

class QuestoesRegistos(models.Model):
    tipoderegisto = models.ForeignKey(TipoRegistos, on_delete=models.SET_NULL, null=True)
    questao = models.CharField(max_length=500, null=True)

    class Meta: verbose_name_plural = "Registos - Questões"

    def __str__(self):
        return self.questao

class Registos(models.Model):
    dataregisto = models.DateField(auto_now=False, auto_now_add=False)
    tiporegisto = models.ForeignKey(TipoRegistos, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(null=False)
    
    class Meta: verbose_name_plural = "Registos"

    def __str__(self):
        return str(self.tiporegisto) + ' - ' + str(self.dataregisto)

class RegistosRespostas(models.Model):
    registo = models.ForeignKey(Registos, on_delete=models.SET_NULL, null=True)
    questao = models.ForeignKey(QuestoesRegistos, on_delete=models.SET_NULL, null=True,  related_name='teste')
    resposta = models.CharField(max_length=50, null=True)

    class Meta: verbose_name_plural = "Registos - Respostas"

