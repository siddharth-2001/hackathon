from django.db import models
from django.contrib.auth.models import AbstractUser 
from products.models import Products

class CustomUser(AbstractUser):
    contact      = models.BigIntegerField(null=True)
    product_list = models.ManyToManyField(Products)
    budget       = models.IntegerField(null=True)

