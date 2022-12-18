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

class Review(models.Model):
    review = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateField(auto_now=True)
