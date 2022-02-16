from django.db import models


class Record(models.Model):
    name_of_fish = models.TextField()
    weight = models.FloatField()
    length = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    species = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    photo = models.ImageField(upload_to='images/')
