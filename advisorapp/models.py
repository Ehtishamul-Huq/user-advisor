from django.db import models

class Advisor(models.Model):
    advisor_name = models.CharField(max_length=100, blank=False, unique=True)
    advisor_photo = models.ImageField(upload_to='images/',blank=False)
    
    

class AdvisorBooking(models.Model):
    advisor = models.ForeignKey(Advisor,on_delete=models.CASCADE, null=True)
    booking_time = models.DateTimeField(blank=False)