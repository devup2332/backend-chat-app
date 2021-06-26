from api.views.GetChat import TokenAuthentication
from api.models.User import User
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models.Chat import Chat
from rest_framework.permissions import IsAuthenticated
from chatProject.settings import pusher_client
from api.serializers.ChatSerializer import ChatSerilizer

class CreateChatView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        user_1 = request.user
        user_2 = User.objects.filter(id=request.data['id']).first()
        chat = ( Chat.objects.filter(user_1=user_1) & Chat.objects.filter(user_2=user_2) ) | ( Chat.objects.filter(user_1=user_2) & Chat.objects.filter(user_2=user_1) )

        if chat:
            return Response("Chat exist")

        chat = Chat.objects.create(user_1=user_1,user_2=user_2)
        chat = ChatSerilizer(chat)
        pusher_client.trigger('chat','new-chat',{
                "chat": chat.data
        })
        return Response("Chat created")