from api.models.Chat import Chat
from rest_framework.authentication import BaseAuthentication
from api.models.Message import Message
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import jwt
from django.conf import settings
from api.models.User import User
from rest_framework.exceptions import AuthenticationFailed
from chatProject.settings import pusher_client
from api.serializers import MessageSerializer

class TokenAuthentication(BaseAuthentication):

    def authenticate(self, request):
        token = request.META['HTTP_AUTHORIZATION'][7:]
        payload = jwt.decode(token,settings.SECRET_KEY,algorithms="HS256")
        
        user:User = User.objects.filter(id=payload['user_id']).first()
        if not user:
            raise AuthenticationFailed("No user wtf")
        user.is_authenticated = True
        return (user,None)

class NewMessage(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        message = request.data['message']['message']
        chat = Chat.objects.filter(id=request.data['id']).first()
        message = Message.objects.create(message=message,emitter=request.user,chat=chat)
        message = MessageSerializer(message)
        chat.last_message = message.data['message']
        chat.save()

        pusher_client.trigger('chat','new-message-user',{
                "message": message.data
        })
        
        return Response("Message has been send successfully")