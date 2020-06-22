from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from vehicles.models import Vehicle

# Model for drug
class Drug(models.Model):

    # Attributes of each drug
    unit = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date = models.DateField()
    shift_hours = models.DurationField()
    rsi_kit_seal_number = models.CharField(max_length=5)
    expiration_date = models.DateField()
    incident_number = models.CharField(max_length=9)
    hospital_number = models.CharField(max_length=5)
    provider_name = models.CharField(max_length=30)
    contact_bc_cole = models.DateTimeField()

    # Redirecting after created
    def get_absolute_url(self):
        return reverse('drug-detail', kwargs={'pk' : self.pk})