from pathlib import Path
from django.urls import path
from . import views

urlpatterns=[
    path('', views.getRoutes, name='routes'),
    path('suppliers/', views.getSuppliers, name='fornecedores'),
    path('suppliers/<str:pk>/', views.getSupplier, name='fornecedor'),
]
