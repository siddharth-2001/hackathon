from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=150)
    brand = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    count_stock = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    review_list = models.TextField()
    rating = models.FloatField()

    def __str__(self):
        return self.name