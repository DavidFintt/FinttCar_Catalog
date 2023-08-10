from rest_framework import serializers
from .models import Manufacturer, Vehicles
from .validators import VehiclesValidators


class vehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicles
        fields = ['year', 'model', 'capacity', 'manufacturer']
    # id = serializers.IntegerField()
    manufacturer = serializers.StringRelatedField(
        read_only=True
    )
    # year = serializers.IntegerField()
    # model = serializers.CharField(max_length=20)
    # capacity = serializers.IntegerField()

    def validate(self, attrs):
        VehiclesValidators(data=attrs, ErrorClass=serializers.ValidationError)
        return super().validate(attrs)
