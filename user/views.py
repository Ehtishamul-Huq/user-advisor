from rest_framework import status, generics
from rest_framework.generics import CreateAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from user.serializers import UserRegistrationSerializer, UserLoginSerializer
from .models import User
from django.contrib.sites.shortcuts import get_current_site
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import update_last_login
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings

class UserRegistrationView(CreateAPIView):

    serializer_class = UserRegistrationSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        jwt_token = RefreshToken.for_user(user)
        user_data.update({'token': str(jwt_token.access_token)})
        return Response({'id': user_data['id'], 'token':user_data['token']}, status=status.HTTP_201_CREATED)


class UserLoginView(generics.GenericAPIView):

    serializer_class = UserLoginSerializer
    
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            obj = User.objects.get(email=self.request.data['email'])
            user_serializer = UserLoginSerializer(obj)
            if obj.password != request.data['password']:
                return Response({'message':'check the correct password'},status=status.HTTP_401_UNAUTHORIZED)
            jwt_token = RefreshToken.for_user(obj)
            token = str(jwt_token.access_token)
            update_last_login(None, obj)
            return Response({
                "id": user_serializer.data['id'],
                'token' : token,
                }, 
                status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'Message':'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)