from re import search
from api.serializers.UserLoginSerializer import UserLoginSerializer
from api.serializers.UserChatSerializer import UserChatSerializer
from api.models.UserChat import UserChat
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from chatProject.settings import pusher_client

class LoginView(APIView):

    def post(self,request):
        serializer = UserLoginSerializer(data=request.data)
        
        if serializer.is_valid():
            user = UserChat.objects.filter(email=request.data['email']).first()
            user.status = True
            user.save()
            serializer_2 = UserChatSerializer(user)
            token = RefreshToken.for_user(user)
            pusher_client.trigger('chat','login-user',{
                "message": "user logged now",
            })
            res = {
                "refresh": str(token),
                "access": str(token.access_token)
            }
            return Response(res)
        

        return Response(serializer.errors)