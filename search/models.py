from django.db import models
from django.contrib.auth.models import User


class Products(models.Model):
    barcode = models.BigIntegerField(primary_key=True)
    image = models.URLField(null=True, default=None, blank=True)
    name = models.CharField(max_length=120)
    category = models.TextField(null=True, default=None, blank=True)
    nutriscore = models.CharField(max_length=5)
    favourites = models.ManyToManyField(User)

    def __str__(self):
        return self.name
