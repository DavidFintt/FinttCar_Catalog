from django.urls import path, include
from vehicles.views import *
from rest_framework.routers import SimpleRouter

registerVehicleRouter = SimpleRouter()
registerVehicleRouter.register(
    'vehicleList/api/v1',
    vehicleList
)

urlpatterns = [
#     path('vehicleList/api/v1/',
#          lista_veiculos,         name="lista_veiculos"),
#     path('vehicleList/api/v1/<int:id>',
#          detalhes_veiculo,       name="detalhes_veiculo")

     path('', include(registerVehicleRouter.urls))
]

