from pathlib import Path
from django.urls import path
from . import views
from .views import MyTokenObtainPairView
# from .views import SupplierFiniteView, SupplierDetailAPIView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns=[

#############################
#  SINGLE PAGES  #
#############################  

    path('', views.getRoutes, name='routes'),

#############################
#  SUPPLIERS  #
#############################  

    path('suppliers/', views.getSuppliers, name='fornecedores'),    
    path('suppliers/create/', views.createSupplier, name='create-fornecedor'),
    path('suppliers/<str:pk>/update/', views.updateSupplier, name='update-fornecedor'),
    path('suppliers/<str:pk>/', views.getSupplier, name='fornecedor'),

#############################
#  REGISTOS  #
#############################    

    path('records/', views.getRecords, name='registos'),
    path('records/create/', views.createRecord, name='create-registo'),
    path('records/<str:pk>/update/', views.updateRecord, name='update-registo'),
    path('records/<str:pk>/', views.getRecord, name='update-registo'),

#############################
#  AUTHENTICATION  #
#############################

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # path("finite/", SupplierFiniteView.as_view(), name="search-fornecedor"),
    # path("finite/<int:id>", SupplierDetailAPIView.as_view(), name="searchId-fornecedor")
]
