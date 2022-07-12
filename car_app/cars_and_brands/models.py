from enum import unique
from django.db import models

# Create your models here. 1, 3, 4, 5



class Car_brand(models.Model):
    name = models.CharField(max_length=99, unique=True)
    details = models.CharField(max_length=99)


class Car(models.Model):
    name = models.CharField(max_length=99)
    brand = models.ForeignKey(Car_brand, on_delete=models.CASCADE, related_name='cars', null=True)
    number_of_doors = models.CharField(max_length=99)
    engine_type = models.CharField(max_length=99)


    
    

