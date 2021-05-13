import re
from .serializers import AdvisorSerializer, AdvisorBookingSerializer
from user.serializers import UserRegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Advisor, AdvisorBooking
from user.models import User

# Create your views here.
class AdvisorAdmin(APIView):
    serializer_class = AdvisorSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)

class AdvisorView(APIView):
    serializer_class = AdvisorSerializer
    def get(self,request,pk):
        try:
            queryset = User.objects.get(id=pk)
            if queryset:
                obj = Advisor.objects.all()
                serializer = self.serializer_class(obj, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'message':'User does not exist.'}, status=status.HTTP_400_BAD_REQUEST)




######################  DOUBT #############
class AdvisorBookingView(APIView):
    serializer_class = AdvisorBookingSerializer
    def get_object(self,advisor_id):
        try:
            return Advisor.objects.get(id=advisor_id)
        except Advisor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, pk, advisor_id, format=None):
        #imp/ort pdb;pdb.set_trace()
        #advisor_id = kwargs.get('advisor_id') 
        #obj = Advisor.objects.get(id=advisor_id)
        #advise = self.get_object(advisor_id)
        #_data = {**request.data, **{"advise":advise}}
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AdvisorDetail(APIView):
    serializer_class = AdvisorBookingSerializer
    def get(self,request,pk):
        #import pdb;pdb.set_trace()
        obj = AdvisorBooking.objects.filter(user=pk)
        serializer = self.serializer_class(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)