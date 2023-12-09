from rest_framework import serializers
from .models import Manufacturer, Vehicles
from .validators import VehiclesValidators
from django.core.files.storage import default_storage
import os


class vehiclesSerializer(serializers.ModelSerializer):
    img_profile = serializers.SerializerMethodField()
    img_2 = serializers.SerializerMethodField()
    class Meta:
        model = Vehicles
        fields = ['id', 'year', 'model', 'capacity', 'price', 'manufacturer', 'dealership','amount', 'highlights', 'img_profile', 'img_2', 'name']

    manufacturer = serializers.StringRelatedField()
    dealership = serializers.StringRelatedField()
    

    def validate(self, attrs):
        VehiclesValidators(data=attrs, ErrorClass=serializers.ValidationError)
        return super().validate(attrs)

    def get_img_profile(self, obj):
        request = self.context.get('request')
        imgurl= request.build_absolute_uri(obj.img_profile.url)
        return imgurl
    
    def get_img_2(self, obj):
        request = self.context.get('request')
        imgurl= request.build_absolute_uri(obj.img_2.url)
        print(imgurl)
        return imgurl