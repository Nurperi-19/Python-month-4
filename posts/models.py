from django.db import models

# Create your models here.

class Post(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.FloatField()
    created_date = models.DateField(auto_now=True)
    modified_date = models.DateField(auto_now_add=True)


# class Product(models.Model):
#     category = models.CharField(max_length=255)
#     image = models.ImageField(blank=True, null=True)
#     name = models.CharField(max_length=255)
#     color = models.TextField()
#     description = models.TextField()
#     rate = models.FloatField()
#     price = models.FloatField()

