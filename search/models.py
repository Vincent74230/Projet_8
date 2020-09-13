from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    barcode = models.BigIntegerField(primary_key=True)
    category = models.CharField(max_length=25)
    name = models.CharField(max_length=120)
    nutriscore = models.CharField(max_length=5)
    favourites = models.ManyToManyField(User)

    def __str__(self):
        return self.name