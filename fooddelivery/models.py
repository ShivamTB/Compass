from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurants(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    cuisine = models.CharField(max_length=128, default='Fast Food')
    description = models.CharField(max_length=256, blank=True, null=True)
    image = models.CharField(max_length=256, blank=True, null=True)

class MenuItems(models.Model):
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=False, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.CharField(max_length=256, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    seat = models.CharField(max_length=5)
