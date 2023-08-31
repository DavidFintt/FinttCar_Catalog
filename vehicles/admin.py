from django.contrib import admin
from .models import Vehicles, Manufacturer, Dealership, Users
# Register your models here.

admin.site.register(Vehicles)
admin.site.register(Manufacturer)
admin.site.register(Dealership)
admin.site.register(Users)