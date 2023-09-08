from django.urls import path, include
from Users.views.api import *
from rest_framework.routers import SimpleRouter


usersRouter = SimpleRouter()
usersRouter.register(
    'users/api/v1',
    usersApi,
    basename='users-api'
)

urlpatterns = [
#     path('vehicleList/api/v1/',
#          lista_veiculos,         name="lista_veiculos"),
#     path('vehicleList/api/v1/<int:id>',
#          detalhes_veiculo,       name="detalhes_veiculo")

    path('', include(usersRouter.urls))
]

