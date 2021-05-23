from rest_framework import serializers
from api.models.UserChat import UserChat
from api.serializers.AvatarSerializer import AvatarSerializer


class UserChatSerializer(serializers.ModelSerializer):
    avatar = AvatarSerializer()
    class Meta:
        model = UserChat
        fields = ['email','phone','avatar']