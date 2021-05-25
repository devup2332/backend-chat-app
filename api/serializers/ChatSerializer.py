
from api.serializers.MessageSerializer import MessageSerializer
from api.serializers.UserChatSerializer import UserChatSerializer
from rest_framework import serializers
from api.models.Chat import ChatModel

class ChatSerilizer(serializers.ModelSerializer):
    last_message =MessageSerializer()
    user_1 = UserChatSerializer()
    user_2 = UserChatSerializer()
    
    class Meta:
        model = ChatModel
        fields = ['id','last_message','user_1','user_2']



