from django.core.exceptions import ValidationError


class VehiclesValidators:
    def __init__(self, data, errors=None, ErrorClass=None):
        self.errors = {} if errors is None else errors
        self.ErrorClass = ValidationError if ErrorClass is None else ErrorClass
        self.data = data
        self.clean()

    def clean(self, *args, **kwargs):
        cd = self.data
        year = str(cd.get('year'))

        if len(year) > 4:
            self.errors.update({'year': 'Lenght of year is greater than 4'})

        if self.errors:
            raise self.ErrorClass(self.errors)
