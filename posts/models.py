from django.db import models

# Create your models here.

class Post(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.FloatField()
    created_date = models.DateField(auto_now=True)
    modified_date = models.DateField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateField(auto_now=True)

