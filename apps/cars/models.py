from django.db import models


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    seats = models.IntegerField()
    type_of_car = models.CharField(max_length=255)
    volume = models.FloatField()
