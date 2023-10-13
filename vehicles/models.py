from django.db import models
from django.contrib.auth.models import AbstractUser
from string import ascii_letters
import random
import os

# Create your models here.

def renameImage(instance,filename):
    idVehicle = instance.pk
    extension = os.path.splitext(filename)[1]
    new_name = f'{idVehicle}{extension}' 
    return new_name

class Users(AbstractUser):
    dealership = models.ForeignKey('Dealership', on_delete=models.CASCADE, related_name="user_dealership", null=True)

class Dealership(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

class Vehicles(models.Model):
    img = models.ImageField(upload_to=renameImage)
    highlights = models.BooleanField(default=False)
    new = models.BooleanField(default=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    year = models.IntegerField()
    model = models.CharField(max_length=20)
    capacity = models.IntegerField()
    amount = models.IntegerField()
    price = models.IntegerField()
    dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.model
    

