from django.shortcuts import render
import requests
from rest_framework.views import APIView
from custom_admin.serializers import AdminRegistrationSerilaizer,ProfileSerializer
from rest_framework.response import Response
from rest_framework import status
from custom_admin.models import Admins
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class RegisterView(APIView):

    def post(self,request):
        serializer=AdminRegistrationSerilaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"success"},status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"failure"},status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    def post(self,request):
        data=request.data
        username=data.get('username')
        password=data.get('password')
        try:
            user=Admins.objects.get(username=username)
            if check_password(password,user.password):
                refresh=RefreshToken.for_user(user)
                return Response({
                    'access_token':str(refresh.access_token),
                    'refresh_token':str(refresh)
                },
                status=status.HTTP_200_OK)
            else:
                return Response({"error":"incorrect password"},status=status.HTTP_401_UNAUTHORIZED)
        except Admins.DoesNotExist:
            return Response({"error":"Admin Doesn't Exists"},status=status.HTTP_404_NOT_FOUND)


class ProfileView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        print("get")
        try:
            user=request.user
            serializer=ProfileSerializer(user)
            return Response(serializer.data)
        except Exception as e:
            return Response({"message":f"{e}"},status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        try:
            serializer=ProfileSerializer(
                request.user,
                data=request.data,
                partial=True
                )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_304_NOT_MODIFIED)
        except Exception as e:
            return Response({"error":f"the error is {e}"},status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request):
        try:
            refresh_token=request.data.get('refresh_token')
            if not refresh_token:
                return Response({"message":"refresh token not send"},status=status.HTTP_400_BAD_REQUEST)
            token=RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message":"Log Out Successfully"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":f"the error is {e}"},status=status.HTTP_400_BAD_REQUEST)

class Getallusersview(APIView):

    def get(self,request):
        user_service_url='https://users-1wfh.onrender.com/api/register'
        response=requests.get(user_service_url)
        filtered_users=[]
        for x in response.json():
            if x.get('role')=='user':
                filtered_users.append(x)
        return Response(filtered_users,status=status.HTTP_200_OK)

class GetallresellersView(APIView):

    def get(self,request):
        reseller_service_url="https://users-1wfh.onrender.com/api/register"
        response=requests.get(reseller_service_url)
        filtered_users=[]
        for x in response.json():
            if x.get('role')=='reseller':
                filtered_users.append(x)
        return Response(filtered_users,status=status.HTTP_200_OK)



