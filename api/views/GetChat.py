from api.models.Message import Message
from django.conf import settings
from api.models.User import User
import jwt
from rest_framework.authentication import BaseAuthentication
from api.serializers.ChatSerializer import ChatSerilizer
from api.models.Chat import Chat
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed

class TokenAuthentication(BaseAuthentication):

    def authenticate(self, request):
        token = request.META['HTTP_AUTHORIZATION'][7:]
        payload = jwt.decode(token,settings.SECRET_KEY,algorithms="HS256")
        
        user:User = User.objects.filter(id=payload['user_id']).first()
        if not user:
            raise AuthenticationFailed("No user wtf")
        user.is_authenticated = True
        return (user,None)

class GetChatView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,id):
        chat = Chat.objects.filter(id=id).first();
        messages = Message.objects.filter(chat=chat)
        chat.messages.set(messages)
        data = ChatSerilizer(chat)
        return Response(data.data)
