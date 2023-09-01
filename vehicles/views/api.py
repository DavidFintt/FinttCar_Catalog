from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ..models import Vehicles, Manufacturer
from ..serializers import vehiclesSerializer
from ..permissions import IsPartDealhersip
from django.shortcuts import get_list_or_404, get_object_or_404

class vehiclePagination(PageNumberPagination):
    page_size = 2

class vehicleList(ModelViewSet):
    queryset = Vehicles.objects.all().select_related('manufacturer')
    serializer_class = vehiclesSerializer
    pagination_class = vehiclePagination
    # permission_classes = [IsAuthenticatedOrReadOnly, ]

    def get_queryset(self):
        qs = super().get_queryset()

        manufacturer_id = self.request.query_params.get('manufacturer_id', None)
        if manufacturer_id is not None:
            manufacturer = Manufacturer.objects.get(pk=manufacturer_id)
            qs = qs.filter(manufacturer=manufacturer)

        return qs
    
    def get_object(self):
        pk = self.kwargs.get('pk')

        if self.request.method == 'GET':
            obj = get_object_or_404(
                self.get_queryset(),
                pk=pk
            )
        

        self.check_object_permissions(self.request, obj)
        return obj
    
    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE', 'UPDATE']:
            return [IsPartDealhersip(), ]
        elif self.request.method == "CREATE":
            method = "create"
            return [IsPartDealhersip(method), ]
        else:
            return [IsAuthenticatedOrReadOnly()]

    def list(self, request, *args, **kwargs):
        vehicles = self.get_queryset()
        serializer = vehiclesSerializer(
            instance= vehicles,
            many=True
            )
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, *args, **kwargs):
        vehicles = self.get_queryset().get(pk=kwargs['pk'])
        serializer = vehiclesSerializer(
            instance=vehicles,
            many=False
            # data=request.data,
            # partial=True
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def partial_update(self, request, *args, **kwargs):
        vehicles = self.get_object()
        serializer = vehiclesSerializer(
            instance=vehicles,
            many=False,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.error_messages, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def create(self, request, *args, **kwargs):
        vehicles = self.get_queryset()
        serializer = vehiclesSerializer(
            # instance=vehicles,
            data=request.data,
            many=False,
        )
        manufacturer_id = request.data['manufacturer']
        if manufacturer_id is not None:
            manufacturer = Manufacturer.objects.get(pk=manufacturer_id)
            if serializer.is_valid(raise_exception=False):
                serializer.save(
                    manufacturer=manufacturer,
                )
                return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
