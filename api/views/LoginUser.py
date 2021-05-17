from re import search
from api.serializers.UserLoginSerializer import UserLoginSerializer
from api.models.UserChat import UserChat
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import AccessToken,RefreshToken
from rest_framework import status

class LoginView(APIView):

    def post(self,request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            print("HERERERERE")
            user = UserChat.objects.filter(email=request.data['email']).first()
            print(user)
            token = RefreshToken.for_user(user)
            res = {
                "refresh": str(token),
                "access": str(token.access_token)
            }
            return Response(res)
        

        return Response(serializer.errors,status=status.HTTP_401_UNAUTHORIZED)