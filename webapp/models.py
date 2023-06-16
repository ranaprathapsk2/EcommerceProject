from django.db import models

# Create your models here.

class SigninDB(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="ProfilePic")
    Password = models.CharField(max_length=100, null=True, blank=True)

class CartDB(models.Model):
    UserName = models.CharField(max_length=100, null=True, blank=True)
    ProductName = models.CharField(max_length=100, null=True, blank=True)
    ProductDescription = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    Total = models.IntegerField(null=True, blank=True)

class CheckoutDB(models.Model):
    FirstName = models.CharField(max_length=100, null=True, blank=True)
    LastName = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.IntegerField(null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Country = models.CharField(max_length=100, null=True, blank=True)
    State = models.CharField(max_length=100, null=True, blank=True)
    Pin = models.IntegerField(null=True, blank=True)
    Street = models.CharField(max_length=200, null=True, blank=True)
    Apartment = models.CharField(max_length=200, null=True, blank=True)