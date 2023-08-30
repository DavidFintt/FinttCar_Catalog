from rest_framework import serializers
from .models import Manufacturer, Vehicles
from .validators import VehiclesValidators


class vehiclesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicles
        fields = ['id', 'year', 'model', 'capacity', 'manufacturer', 'dealership','amount']

    manufacturer = serializers.StringRelatedField()
    dealership = serializers.StringRelatedField()

    def validate(self, attrs):
        VehiclesValidators(data=attrs, ErrorClass=serializers.ValidationError)
        return super().validate(attrs)
