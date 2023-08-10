from django.db import models

# Create your models here.


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

    def __str__(self) -> str:
        return self.model
