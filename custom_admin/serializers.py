from rest_framework import serializers
from custom_admin.models import Admins
from django.contrib.auth.hashers import make_password

class AdminRegistrationSerilaizer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    class Meta:
        model=Admins
        fields=['name','mobile_number','email','password','profile_pic','username']
    
    def create(self,validate_data):
        hashed= make_password(validate_data['password'])
        validate_data['password']=hashed
        return Admins.objects.create(**validate_data)


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=Admins
        fields=['name','mobile_number','email','password','profile_pic','username']