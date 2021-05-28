from api.models.Avatar import Avatar
from rest_framework import serializers
from api.models.User import User
from api.serializers.AvatarSerializer import AvatarSerializer

class UserSerializer(serializers.ModelSerializer):
    avatar = AvatarSerializer()
    class Meta:
        model = User
        fields = ['avatar','id','email','last_name','first_name','status']
    
    
