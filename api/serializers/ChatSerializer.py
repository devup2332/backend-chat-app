from functools import partial
from rest_framework import serializers
from api.models.Chat import Chat
from api.serializers.UserSerializer import UserSerializer
from api.serializers.MessageSerializer import MessageSerializer

class ChatSerilizer(serializers.ModelSerializer):
    user_1 = UserSerializer()
    user_2 = UserSerializer()
    messages = MessageSerializer(many=True,required=False)
    
    class Meta:
        model = Chat
        fields = '__all__'
