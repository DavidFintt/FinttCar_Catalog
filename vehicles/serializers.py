from rest_framework import serializers
from .models import Manufacturer, Vehicles
from .validators import VehiclesValidators
from django.core.files.storage import default_storage
from os.path import abspath


class vehiclesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vehicles
        fields = ['id', 'year', 'model', 'capacity', 'price', 'manufacturer', 'dealership','amount', 'highlights', 'img']

    manufacturer = serializers.StringRelatedField()
    dealership = serializers.StringRelatedField()
    

    def validate(self, attrs):
        VehiclesValidators(data=attrs, ErrorClass=serializers.ValidationError)
        return super().validate(attrs)

    # def get_img(self, obj):
    #     request = self.context.get('request')
    #     if obj.img:
    #         img_path = abspath(obj.img.path)
    #         return request.build_absolute_uri(img_path)
    #     return None