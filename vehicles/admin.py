from django.contrib import admin
from .models import Vehicles, Manufacturer, Dealership
# Register your models here.

admin.site.register(Vehicles)
admin.site.register(Manufacturer)
admin.site.register(Dealership)
