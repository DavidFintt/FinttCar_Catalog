from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from ..models import Vehicles, Manufacturer
from ..serializers import vehiclesSerializer
from django.shortcuts import get_list_or_404, get_object_or_404

class vehiclePagination(PageNumberPagination):
    page_size = 2

class vehicleList(ModelViewSet):
    queryset = Vehicles.objects.all().select_related('manufacturer')
    serializer_class = vehiclesSerializer
    pagination_class = vehiclePagination

    def List(self, request, *args, **kwargs):
        vehicles = self.get_queryset()
        serializer = vehiclesSerializer(
            instance= vehicles,
            many=True
            )
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def Retrieve(self, request, *args, **kwargs):
        vehicles = self.get_queryset()
        serializer = vehiclesSerializer(
            instance=vehicles,
            many=False,
            # data=request.data,
            # partial=True
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def partial_update(self, request, *args, **kwargs):
        vehicles = self.get_queryset()
        serializer = vehiclesSerializer(
            instance=vehicles,
            many=False,
            data=request.data,
            partial=True
        )
        serializer.is_valid()
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        vehicles = self.get_queryset()
        serializer = vehiclesSerializer(
            # instance=vehicles,
            data=request.data,
            many=False,
        )
        print(request.data)
        print(request.data)
        print(request.data)
        print(request.data)
        manufacturer_id = request.data['manufacturer']
        if manufacturer_id is not None:
            manufacturer = Manufacturer.objects.get(pk=manufacturer_id)
            if serializer.is_valid(raise_exception=False):
                serializer.save(
                    manufacturer=manufacturer,
                )
                return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# @api_view(http_method_names=['get', 'post'])
# def lista_veiculos(request):

#     if request.method == 'GET':
#         vehiclesList = Vehicles.objects.all().select_related('manufacturer')
#         serializerVehicle = vehiclesSerializer(
#             instance=vehiclesList, many=True)
#         return Response(serializerVehicle.data)

#     elif request.method == 'POST':
#         serializer = vehiclesSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save(
#                 manufacturer=Manufacturer.objects.get(
#                     id=request.data['manufacturer']),
#             )

#             return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# @api_view(http_method_names=['get', 'put'])
# def detalhes_veiculo(request, id):
#     if request.method == 'GET':
#         try:
#             Vehicles.objects.get(pk=id)
#         except:
#             return Response({
#                 'detail': 'Not found man'
#             }, status=status.HTTP_418_IM_A_TEAPOT)
#         else:
#             vehicleDetail = Vehicles.objects.select_related('manufacturer').get(
#                 pk=id)
#             serializerVehicle = vehiclesSerializer(
#                 instance=vehicleDetail, many=False)
#             return Response(serializerVehicle.data)
#     elif request.method == 'PUT':
#         serializer = vehiclesSerializer(data=request.data)
#         if serializer.is_valid():
#             return Response(serializer.validated_data, status=status.HTTP_206_PARTIAL_CONTENT)
#         return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
