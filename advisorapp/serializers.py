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
    #profile = AdvisorSerializer(required=False, read_only=True)
    #userprofile = UserRegistrationSerializer(many=True, required=False, read_only=True)
    #booking_time = serializers.DateTimeField()
    class Meta:
        model = AdvisorBooking
        fields = ('id','user','advisor', "booking_time")
        #fields = '__all__'
        #extra_kwargs = {'user':{'read_only':True}, 'advisor':{'read_only':True}}
        #depth = 1

class AdvisorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvisorBooking
        fields = ('id','user','advisor', "booking_time")
        depth = 1