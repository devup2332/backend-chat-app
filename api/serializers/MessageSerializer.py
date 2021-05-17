from rest_framework import serializers
from api.models.Message import MessageModel

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields = '__all__'