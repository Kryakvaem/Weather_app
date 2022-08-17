from django.db import models
from django.utils import timezone

class City (models.Model):
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return self.city_name

class Weather (City):
    data = models.DateField(default=timezone.now())
    temperature = models.FloatField()

    def get_weather(self):
        print("jhj")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.city_name
