from typing import Any
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=100)
    phone = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.username

    
class CategoryModel(models.Model):
    choice_text=models.CharField(max_length=100)

    def __str__(self):
        return self.choice_text


class ProductModel(models.Model):
    prodname=models.CharField(max_length=100)
    category=models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    price=models.FloatField()
    image=models.ImageField(upload_to='productpics', null=True, blank=True, default='/productpics/default.jpg')
    stock=models.IntegerField(default=0)
    availability=models.CharField(max_length=20, choices=(('In Stock', 'In stock'),('Out of Stock','Out of Stock')), default='Out of Stock')

    def __str__(self):
        return self.prodname
     




class PostModel(models.Model):
    feed = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post #{self.id}'




class FeedModel(models.Model):
    text = models.TextField(max_length=255)

    def __str__(self):
        return self.text
    