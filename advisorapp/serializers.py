from rest_framework import serializers
from .models import Advisor, AdvisorBooking
from user.models import User
from django.db import models
from datetime import datetime
from user.serializers import UserRegistrationSerializer
from rest_framework.reverse import reverse
#from .views import AdvisorView, AdvisorBookingView

class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = ('id','advisor_name','advisor_photo')

class AdvisorBookingSerializer(serializers.ModelSerializer):
    #profile = AdvisorSerializer(many=True, read_only=True)
    class Meta:
        model = AdvisorBooking
        fields = ('id', "booking_time")

    #def create(self, validated_data):
     #   profile = validated_data.pop('profile')
      #  user = AdvisorSerializer.create(AdvisorSerializer(), validated_data=user_data)
       # student, created = UnivStudent.objects.update_or_create(user=user,
        #                    subject_major=validated_data.pop('subject_major'))
        #return student