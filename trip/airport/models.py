from django.db import models


class DistanceComputeResponse(models.Model):
    first_airport_code = models.CharField(max_length=3)
    second_airport_code = models.CharField(max_length=3)
    distance = models.DecimalField(max_length=15, decimal_places=3, max_digits=15)

    def __init__(self, first_airport_code, second_airport_code, distance, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.first_airport_code = first_airport_code
        self.second_airport_code = second_airport_code
        self.distance = distance
