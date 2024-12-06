from django.db import models
from .models import *

# Create your models here.
class Contact_Us(models.Model):
    Name       =models.CharField(max_length=100)  
    Email      =models.EmailField(blank=True)
    Id         =models.IntegerField(blank=True)

    def __str__(self):
        return self.Name
