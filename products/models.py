from django.db import models

# Create your models here.

class Product(models.Model):
    category = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=255)
    color = models.TextField()
    description = models.TextField()
    rate = models.FloatField()
    price = models.FloatField()
