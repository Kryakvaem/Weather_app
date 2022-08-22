from django.db import models
from django.utils import timezone

class City(models.Model):
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return self.city_name

class Weather (models.Model):
    city_name_weather = models.ForeignKey(City, on_delete=models.CASCADE)
    data = models.DateField()
    temperature = models.FloatField()
    time = models.TimeField()

    def __str__(self):
        return str(self.city_name_weather)
