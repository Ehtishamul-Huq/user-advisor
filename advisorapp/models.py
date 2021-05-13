from django.db import models
from user.models import User
import uuid

class Advisor(models.Model):
    advisor_name = models.CharField(max_length=100, blank=False, unique=True)
    advisor_photo = models.ImageField(upload_to='images/',blank=False)
    
    def __str__(self):
        return self.advisor_name

class AdvisorBooking(models.Model):
    advisor = models.ForeignKey(Advisor,on_delete=models.CASCADE, null=True)
    booking_time = models.DateTimeField(blank=False)

    def __str__(self):
        return self.advisor.advisor_name