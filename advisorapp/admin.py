from django.contrib import admin
from .models import Advisor, AdvisorBooking
# Register your models here.
@admin.register(Advisor)
class AdvisorAdmin(admin.ModelAdmin):
    list_display = ['id', 'advisor_name', 'advisor_photo']

@admin.register(AdvisorBooking)
class AdvisorBookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'booking_time']