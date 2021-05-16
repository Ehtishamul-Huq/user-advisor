from django.db import models
from django.db.models.fields import related
from user.models import User

class Advisor(models.Model):
    advisor_name = models.CharField(max_length=100, blank=False, unique=True)
    advisor_photo = models.ImageField(upload_to='images/',blank=False)
    
    def __str__(self):
        return self.advisor_name

class AdvisorBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    advisor = models.ForeignKey(Advisor,on_delete=models.CASCADE)
    booking_time = models.DateTimeField(blank=False)