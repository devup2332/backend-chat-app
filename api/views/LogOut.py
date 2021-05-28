from api.models.User import User
from django.conf import settings
import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from chatProject.settings import pusher_client
from rest_framework.exceptions import AuthenticationFailed

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

class LogOutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self,request):
        user = request.user
        user.status = False
        user.save()
        pusher_client.trigger('chat','logout-user',{
                "message": "User is logout"
        })
        return Response("You are logout")