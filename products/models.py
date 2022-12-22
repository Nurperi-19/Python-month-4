from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=55)
    icon = models.ImageField(blank=True, null=True)

class Product(models.Model):
    category = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=255)
    color = models.TextField()
    description = models.TextField()
    rate = models.FloatField()
    price = models.FloatField()
    categories = models.ManyToManyField(Category)

class Review(models.Model):
    review = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateField(auto_now=True)
