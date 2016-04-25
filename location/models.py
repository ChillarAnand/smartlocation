from django.db import models
from djgeojson.fields import PolygonField
# from django.contrib.postgres.fields import JSONField


class Provider(models.Model):
    name = models.CharField(max_length=100, default='')
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True)
    language = models.CharField(max_length=40, blank=True)
    currency = models.CharField(max_length=3, blank=True)


class ServiceArea(models.Model):
    provider = models.ForeignKey(Provider)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    polygon = PolygonField()
