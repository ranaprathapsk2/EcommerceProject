from django.db import models

# Create your models here.

class CategoryDB(models.Model):
    CategoryName = models.CharField(max_length=70, null=True, blank=True)
    CategoryDescription = models.CharField(max_length=200, null=True, blank=True)
    CategoryImage = models.ImageField(upload_to="CategoryImage")


class ProductDB(models.Model):
    ProductCategory = models.CharField(max_length=100, null=True, blank=True)
    ProductName = models.CharField(max_length=100, null=True, blank=True)
    ProductPrice = models.IntegerField(null=True, blank=True)
    ProductDescription = models.CharField(max_length=200, null=True, blank=True)
    ProductBrand = models.CharField(max_length=100, null=True, blank=True)
    ProductImage = models.ImageField(upload_to="ProductImage")


class contactDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Message = models.CharField(max_length=10000, null=True, blank=True)