from django.db import models

# Create your models here.
from countries_list import countries

from django.db import models


class Client(models.Model):
    CHOICE=[("Male","Male"),("Female","Female")]
    full_name=models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    email=models.EmailField()
    organisation=models.CharField(max_length=50)
    country=models.CharField(max_length=50, choices=countries, default="Nepal")
    phone_number = models.CharField(max_length=50)
    domain=models.SlugField(null=True, blank=True)
    gender=models.CharField(max_length=50, choices=CHOICE)
    date=models.DateField(auto_now_add=True)


    def __str__(self):
        return f"Client: {self.full_name} {self.last_name} {self.date}"