from rest_framework import serializers
from api.models.UserChat import UserChat


class UserChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChat
        fields = '__all__'