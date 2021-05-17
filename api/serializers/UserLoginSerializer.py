from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from api.models.UserChat import UserChat
from rest_framework import serializers


class UserLoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField()   
    
    def validate(self,data):
        user = UserChat.objects.filter(email=data['email']).first()
        if not user:
            raise serializers.ValidationError({"message":"Email dosent exist"})
        match = user.check_password(data['password'])

        if match:
            return user
        raise serializers.ValidationError({"message":"Password is incorrect"})    

