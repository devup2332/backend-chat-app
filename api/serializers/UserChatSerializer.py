from rest_framework import serializers
from api.models.UserChat import UserChat
from api.serializers.AvatarSerializer import AvatarSerializer


class UserChatSerializer(serializers.ModelSerializer):
    avatar = AvatarSerializer()
    class Meta:
        model = UserChat
        fields = ['id','email','phone','avatar','first_name','last_name','status']