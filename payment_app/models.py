from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=[('USD', 'US Dollar'), ('EUR', 'Euro')])

    def __str__(self):
        return self.name

class Order(models.Model):
    items = models.ManyToManyField(Item)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class Discount(models.Model):
    name = models.CharField(max_length=50)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

class Tax(models.Model):
    name = models.CharField(max_length=50)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
