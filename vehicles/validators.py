from django.core.exceptions import ValidationError
from .models import Manufacturer


class VehiclesValidators:
    def __init__(self, data, errors=None, ErrorClass=None):
        self.errors = {} if errors is None else errors
        self.ErrorClass = ValidationError if ErrorClass is None else ErrorClass
        self.data = data
        self.clean_year()
        # self.clean_manufacturer()

    def clean_year(self, *args, **kwargs):
        cd = self.data
        year = str(cd.get('year'))

        if len(year) > 4:
            self.errors.update({'year': 'Lenght of year is greater than 4'})

        if self.errors:
            raise self.ErrorClass(self.errors)

    # def clean_manufacturer(self, *args, **kwargs):
    #     aa = self.data
    #     manufacturer = aa.get('manufacturer')
    #     if Manufacturer.objects.get(id=manufacturer) is None:
    #         self.errors.update({'Manufacturer': 'Manufacturer not exists'})
    #         raise self.ErrorClass(self.errors)
        # try:
        #     Manufacturer.objects.get(id=manufacturer)
        # except:
        #     if len(manufacturer) > 1:
        #         self.errors.update(
        #             {'Manufacturer': 'Manufacturer need just one value, you passed more than one'})
        #     else:
        #         self.errors.update({'Manufacturer': 'Manufacturer not exists'})
        #         raise self.ErrorClass(self.errors)

        # else:
        #     pass
