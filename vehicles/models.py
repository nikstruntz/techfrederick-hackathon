from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Model for vehicle
class Vehicle(models.Model):

    # Attributes of each vehicle
    unit = models.CharField(max_length=30)
    date = models.DateField()
    oil = models.BooleanField()
    transmission_fluid = models.BooleanField()
    brake_fluid = models.BooleanField()
    coolant_fluid = models.BooleanField()
    lucas = models.BooleanField()
    ems_equipment = models.BooleanField()
    suction = models.BooleanField()
    front_left_tire_pressure = models.DecimalField(decimal_places=0, max_digits=2)
    front_right_tire_pressure = models.DecimalField(decimal_places=0, max_digits=2)
    rear_left_tire_pressure = models.DecimalField(decimal_places=0, max_digits=2)
    rear_right_tire_pressure = models.DecimalField(decimal_places=0, max_digits=2)
    provider_name = models.CharField(max_length=30)
    comments = models.TextField()

    # Redirecting after created
    def get_absolute_url(self):
        return reverse('vehicle-detail', kwargs={'pk' : self.pk})

    # Defining the name
    def __str__(self):
        return (self.unit)