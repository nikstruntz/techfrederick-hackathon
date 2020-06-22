from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from vehicles.models import Vehicle

# Model for Vehicle Equipment
class Equipment(models.Model):

    # Attributes for vehicle equipment
    unit = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date = models.DateField()
    mileage = models.DecimalField(decimal_places=0, max_digits=4)
    fuel = models.CharField(max_length=1)
    emergency_lights = models.BooleanField()
    driving_lights = models.BooleanField()
    red_bag = models.BooleanField()
    lp_fifteen = models.BooleanField()
    trans_box = models.BooleanField()
    bls_bag = models.BooleanField()
    rtf_bags = models.BooleanField()
    suction = models.BooleanField()
    oxygen_bag = models.BooleanField()
    signature = models.CharField(max_length=50)

    # Redirecting after created
    def get_absolute_url(self):
        return reverse('equipment-detail', kwargs={'pk' : self.pk})