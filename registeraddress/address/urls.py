from django.urls import path
from .views import Index, RegisterAddress, SearchCEP, AddressIndex

urlpatterns = [
    path('', Index, name='index'),
    path('address/', AddressIndex, name='AddressIndex'),
    path('registeradress/', RegisterAddress, name='RegisterAddress'),
    path('searchcep/', SearchCEP, name='SearchCEP'),
]
