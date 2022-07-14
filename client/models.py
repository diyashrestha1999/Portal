from django.db import models

# Create your models here.
from countries_list import countries

from django.db import models


class Client(models.Model):
    full_name=models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    email=models.EmailField()
    oraganisation=models.CharField(max_length=50)
    country=models.CharField(max_length=50, choices=countries, default="Nepal")
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)


    def __str__(self):
        return f"Client: {self.full_name} {self.last_name}"