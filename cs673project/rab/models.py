from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    open_time = models.CharField(max_length=10)
    close_time = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=30)

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE) #role_id in database
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default = None) #restaurant_id in database

class Dish(models.Model):
    name = models.CharField(max_length=100)
    cook_time = models.IntegerField(default=0)
    fresh_time = models.IntegerField(default=0)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='resources',blank=True,null=True)
    #description = models.CharField(max_length=100)
    serve = models.IntegerField(default=0)

class Menu(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, default=None)
    last_served = models.DateTimeField(null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,default = None)

class Orders(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    last_updated = models.DateTimeField()
