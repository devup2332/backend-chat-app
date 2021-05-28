
from api.models.User import User
from rest_framework import serializers
from django.contrib.auth.hashers import check_password


class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField()   
    
    def validate(self,data):
        user = User.objects.filter(email=data['email']).first()
        if not user:
            raise serializers.ValidationError({"message":"Email dosent exist"})
        print(data['password'])
        match = check_password(data['password'],user.password)

        if match:
            return user
        raise serializers.ValidationError({"message":"Password is incorrect"})  

