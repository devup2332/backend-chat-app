from api.models.Avatar import Avatar
from django.conf import settings
from api.models.User import User
from api.serializers.ChatSerializer import ChatSerilizer
from api.models.Chat import Chat
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
import jwt

class TokenAuthentication(BaseAuthentication):

    def authenticate(self, request):
        token = request.META['HTTP_AUTHORIZATION'][7:]
        payload = jwt.decode(token,settings.SECRET_KEY,algorithms="HS256")
        user:User = User.objects.filter(id=payload['user_id']).first()
        if not user:
            int
            raise AuthenticationFailed("No user wtf")
        user.is_authenticated = True
        return (user,None)

class GetChatsView (APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):

        user = request.user
        chats = Chat.objects.filter(user_1=user) | Chat.objects.filter(user_2=user)
        chats = ChatSerilizer(chats,many=True)
        return Response(chats.data)


