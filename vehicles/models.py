from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Users(AbstractUser):
    dealership = models.ForeignKey('Dealership', on_delete=models.CASCADE, related_name="user_dealership", null=True)

class Dealership(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

class Vehicles(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    year = models.IntegerField()
    model = models.CharField(max_length=20)
    capacity = models.IntegerField()
    amount = models.IntegerField()
    price = models.IntegerField()
    dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.model
