from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Vehicles, Manufacturer
from ..serializers import vehiclesSerializer
from django.shortcuts import get_list_or_404, get_object_or_404


@api_view(http_method_names=['get', 'post'])
def lista_veiculos(request):
    if request.method == 'GET':
        vehiclesList = Vehicles.objects.all().select_related('manufacturer')
        serializerVehicle = vehiclesSerializer(
            instance=vehiclesList, many=True, context={'request', request})
        return Response(serializerVehicle.data)

    elif request.method == 'POST':
        serializer = vehiclesSerializer(
            data=request.data, context={'request', request})
        manufacturer = get_object_or_404(
            Manufacturer, pk=request.data['manufacturer'])
        if serializer.is_valid():
            serializer.save(
                manufacturer=manufacturer,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(http_method_names=['get', 'patch', 'delete'])
def detalhes_veiculo(request, id):
    vehicleDetail = get_object_or_404(
        Vehicles.objects.select_related('manufacturer'),
        pk=id)
    if request.method == 'GET':
        serializerVehicle = vehiclesSerializer(
            instance=vehicleDetail, many=False)
        return Response(serializerVehicle.data)

    elif request.method == 'PATCH':
        serializerVehicle = vehiclesSerializer(
            instance=vehicleDetail, many=False, data=request.data, partial=True)
        serializerVehicle.is_valid(raise_exception=True)
        serializerVehicle.save()
        return Response(serializerVehicle.data)

    elif request.method == 'DELETE':
        vehicleDetail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
