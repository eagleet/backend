from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Fornecedor),
admin.site.register(MP),
admin.site.register(MateriaPrima),
admin.site.register(Receita),
admin.site.register(Alergeneo),
admin.site.register(Produto),
admin.site.register(Lote),
admin.site.register(IngredientesReceita),
admin.site.register(FornecedorContactos),
admin.site.register(TipoRegistos),
admin.site.register(QuestoesRegistos),
admin.site.register(Registos),
admin.site.register(RegistosRespostas),

