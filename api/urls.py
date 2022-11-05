from pathlib import Path
from django.urls import path
from . import views
# from .views import SupplierFiniteView, SupplierDetailAPIView

urlpatterns=[
    path('', views.getRoutes, name='routes'),
    path('suppliers/', views.getSuppliers, name='fornecedores'),    
    path('suppliers/create/', views.createSupplier, name='create-fornecedor'),
    path('suppliers/<str:pk>/update/', views.updateSupplier, name='update-fornecedor'),
    
    path('suppliers/<str:pk>/', views.getSupplier, name='fornecedor'),

    # path("finite/", SupplierFiniteView.as_view(), name="search-fornecedor"),
    # path("finite/<int:id>", SupplierDetailAPIView.as_view(), name="searchId-fornecedor")
]
