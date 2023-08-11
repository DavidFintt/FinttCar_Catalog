from rest_framework import serializers
from .models import Manufacturer, Vehicles
from .validators import VehiclesValidators


class vehiclesSerializer(serializers.ModelSerializer):

    manufacturer = serializers.StringRelatedField()

    class Meta:
        model = Vehicles
        fields = ['id', 'year', 'model', 'capacity', 'manufacturer']

    def validate(self, attrs):
        VehiclesValidators(data=attrs, ErrorClass=serializers.ValidationError)
        return super().validate(attrs)
