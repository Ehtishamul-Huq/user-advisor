from rest_framework import serializers
from .models import Advisor, AdvisorBooking
from user.models import User
from django.db import models
from datetime import datetime
from user.serializers import UserRegistrationSerializer
from rest_framework.reverse import reverse

class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = ('id', 'advisor_name','advisor_photo')


class AdvisorBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvisorBooking
        fields = ('id','user','advisor', "booking_time")

class AdvisorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvisorBooking
        fields = ('id','user','advisor', "booking_time")
        depth = 1