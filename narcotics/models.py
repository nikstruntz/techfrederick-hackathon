from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from vehicles.models import Vehicle

# Model for Narcotics
class Narcotic(models.Model):

    # Attributes of each narcotic
    unit = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date = models.DateField()
    shift_hours = models.DurationField()
    morphine_in_stock = models.DecimalField(decimal_places=0, max_digits=3)
    ketamine_in_stock_hundred_miligram_millileter = models.DecimalField(decimal_places=0, max_digits=5)
    ketamine_in_stock_ten_miligram_millileter = models.DecimalField(decimal_places=0, max_digits=4)
    versed_in_stock = models.DecimalField(decimal_places=0, max_digits=3)
    seal_number = models.DecimalField(decimal_places=0, max_digits=5)
    incident_number = models.CharField(max_length=9)
    medication_used = models.CharField(max_length=5)
    medication_amount_mg = models.DecimalField(decimal_places=0, max_digits=4)
    provider_name = models.CharField(max_length=30)
    waste_witness_initials = models.CharField(max_length=2)
    waste_amount_mg = models.DecimalField(decimal_places=0, max_digits=3)

    # Redirecting after created
    def get_absolute_url(self):
        return reverse('narcotics-detail', kwargs={'pk' : self.pk})