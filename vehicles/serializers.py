from rest_framework import serializers
from .models import Manufacturer, Vehicles
from .validators import VehiclesValidators
from django.core.files.storage import default_storage
import os


class vehiclesSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()
    class Meta:
        model = Vehicles
        fields = ['id', 'year', 'model', 'capacity', 'price', 'manufacturer', 'dealership','amount', 'highlights', 'img', 'name']

    manufacturer = serializers.StringRelatedField()
    dealership = serializers.StringRelatedField()
    

    def validate(self, attrs):
        VehiclesValidators(data=attrs, ErrorClass=serializers.ValidationError)
        return super().validate(attrs)

    def get_img(self, obj):
        request = self.context.get('request')
        imgurl= request.build_absolute_uri(obj.img.url)
        return imgurl