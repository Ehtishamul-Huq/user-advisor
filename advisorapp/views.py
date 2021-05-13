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

class AdvisorBookingView(APIView):
    serializer_class = AdvisorBookingSerializer
    #lookup_field = 'pk'
    #lookup_url_kwarg = 'user_pk'
    def post(self,request, pk, advisor_id):
        #import pdb;pdb.set_trace()
        #adbook = Adbook(user=User.objects.get(id=pk), advisor=Advisor.objects.get(id=advisor_id))
        #queryset = User.objects.get(id=pk)
        #obj = Advisor.objects.get(id=advisor_id)
        #serializer = AdvisorSerializer(obj)
        #user_serializer = UserRegistrationSerializer(queryset)
        #data1 = request.data
        #_data = {**{"time":request.data}, **{"advisor":pk}}
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
       
        #response = {**serializer.data, **advisor_serializer.data, **{"advisor_id": advisor_id}}
        #return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_200_OK)
class AdvisorDetail(APIView):
    serializer_class = AdvisorBookingSerializer
    def get(self,request,pk):
        #import pdb;pdb.set_trace()
        obj = AdvisorBooking.objects.filter(user=pk)
        serializer = self.serializer_class(obj, many=True)
        #advisor_id = serializer.data['advisor']
        #advisor_serializer = AdvisorSerializer(advisor_id)

        return Response(serializer.data, status=status.HTTP_200_OK)