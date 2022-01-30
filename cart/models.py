from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    image = models.ImageField(blank=True)    
    class Meta:
        ordering = ['name']

class Discount(models.Model):
    category = models.CharField(max_length=200)

    class Meta:
        ordering = ['category']