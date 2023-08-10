from django.urls import path
from vehicles.views import *

urlpatterns = [
    path('vehicleList/api/v1/',
         lista_veiculos,         name="lista_veiculos"),
    path('vehicleList/api/v1/<int:id>',
         detalhes_veiculo,       name="detalhes_veiculo")
]
