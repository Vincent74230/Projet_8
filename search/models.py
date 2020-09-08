from django.db import models
from django.contrib.auth.models import User

class food(models.Model):
    barcode = models.IntegerField(primary_key=True)
    stuff_name = models.CharField(max_length=35)
    stuff_category = models.CharField(max_length=35)
    nutriscore = models.CharField(max_length=5)
    favourites = models.ManyToManyField(User)
