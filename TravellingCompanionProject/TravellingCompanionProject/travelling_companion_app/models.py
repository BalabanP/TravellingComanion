
from django.db import models
from datetime import datetime 
# Create your models here.

class Location(models.Model):
    city = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=50, null=False)

    def __str__(self) -> str:
        return self.city
        
class Currencys(models.TextChoices):
        Lei='Lei',('Leu Romanesc')
        EUR='EUR',('Euro')
        USD='USD',('Dolar American')
        GBP='GBP',("U.K. Pound")

class Trip(models.Model):
    name = models.CharField(max_length=50, null=False)
    budget = models.PositiveIntegerField(blank=False)
    currency = models.CharField(
        max_length=7,
        choices=Currencys.choices,
        default=Currencys.Lei)
    comments = models.TextField(max_length=200,blank=True)
    total_budget = models.PositiveIntegerField(blank=True,default=0)


class Flight(models.Model):
    trip = models.ForeignKey(
        Trip, 
        on_delete= models.CASCADE)
    origin_location = models.ForeignKey(
        Location, 
        related_name= 'origin', 
        on_delete= models.CASCADE)
    destination = models.ForeignKey(
        Location,
        related_name= 'destination', 
        on_delete= models.CASCADE)
    date_from = models.DateField(null=False,default=datetime.now)
    time_from = models.TimeField(null=False,default=datetime.now)
    date_to = models.DateField(null=False,default=datetime.now)
    time_to = models.TimeField(null=False,default=datetime.now)
    price = models.PositiveIntegerField(blank=False)
    currency = models.CharField(
        max_length=7,
        choices=Currencys.choices,
        default=Currencys.Lei)
    def __str__(self) -> str:
        return "{}_{}".format(self.origin_location,self.destination)

class Booking(models.Model):
    trip = models.ForeignKey(
        Trip, 
        on_delete= models.CASCADE)
    location = models.ForeignKey(
        Location, 
        on_delete= models.CASCADE)
    date_from = models.DateField(null=False,default=datetime.now)
    time_from = models.TimeField(null=False,default=datetime.now)
    date_to = models.DateField(null=False,default=datetime.now)
    time_to = models.TimeField(null=False,default=datetime.now)
    price = models.PositiveIntegerField(blank=False)
    currency = models.CharField(
        max_length=7,
        choices=Currencys.choices,
        default=Currencys.Lei)
    def __str__(self) -> str:
        return "{}".format(self.location)
