from django.urls import path, include
from Users.views.api import *
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


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
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include(registerVehicleRouter.urls))
]

