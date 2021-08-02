from django.db import models
from django.db.models.base import Model

# Create your models here.

class Contact(models.Model):
    firstName = models.CharField("First name", max_length=255, blank = True, null = True)
    lastName = models.CharField("Last name", max_length=255, blank = True, null = True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank = True, null = True)
    address = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
    
    def __str__(self):
        return self.firstName

class Product(models.Model):
    name = models.CharField("Name", max_length=255, blank = True, null = True)
    price = models.IntegerField("Price", blank=True, null=True)

    def __str__(self):
        return self.name