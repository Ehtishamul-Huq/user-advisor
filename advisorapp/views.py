from .serializers import AdvisorSerializer, AdvisorBookingSerializer, AdvisorDetailSerializer
from user.serializers import UserRegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Advisor, AdvisorBooking
from user.models import User
from datetime import datetime
import json

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
    def get(self, request, *args, **kwargs):
        advisor_id = self.kwargs['advisor_id']
        obj = Advisor.objects.get(id=advisor_id)
        advisor_serializer = AdvisorSerializer(obj)
        pk = self.kwargs['pk']
        queryset = User.objects.get(id=pk)
        user_serializer = UserRegistrationSerializer(queryset)
        return Response({'data': advisor_serializer.data, 'user': user_serializer.data}, status=status.HTTP_200_OK)


   # def get_queryset(self):
    #    uid = self.kwargs['pk']
     #   user = User.objects.get(id=uid)
      #  return user

    def post(self, request, *args, **kwargs):
        #import pdb;pdb.set_trace()
        #d = datetime.fromisoformat(request.data['booking_time'][:-1])
        #date_object = datetime.strptime(request.data['booking_time'][:-1], "%Y-%m-%dT%H:%M")
        #date_object = d.strftime('%Y-%m-%d %H:%M')
        #_data = {**date_object, **{"advisor":advisor_id}}
        #ad = Advisor.objects.get(id=advisor_id)
        #adbook = AdvisorSerializer(ad)
        #obj = self.kwargs['advisor_id']
        #d = Advisor.objects.get(id=obj)
        #da = AdvisorSerializer(d)
        #user_obj = self.kwargs['pk']
        #u = User.objects.get(id=user_obj)
        #ua = UserRegistrationSerializer(u)
        #di = d + u
        #_data = {**{'advisor':da.data}, **{'user':ua.data}, **{'timing':date_object}}
       # _data = {**{'timing':request.data}, **{'advisor': advisor_id}}
        serializer = AdvisorBookingSerializer(data=request.data)
        #serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()    
        # data1 = {**{'advisor':adbook}, **{'data':serializer.data}}
        return Response(status=status.HTTP_200_OK)

class AdvisorDetail(APIView):
    serializer_class = AdvisorDetailSerializer
    def get(self,request,pk):
        obj = AdvisorBooking.objects.filter(user=pk)
        serializer = self.serializer_class(obj, many=True)
        string = json.loads(json.dumps(serializer.data))
        for i in range(len(string)):
            string[i].pop('user')
        string_data = json.loads(json.dumps(string))
        return Response(string_data, status=status.HTTP_200_OK)