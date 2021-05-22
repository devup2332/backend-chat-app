from api.serializers.UserChatSerializer import UserChatSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models.UserChat import UserChat
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import MultiPartParser,FormParser
from cloudinary import uploader,config
from api.models import Avatar
from rest_framework import status

config(cloud_name = "dder8kjda", 
  api_key = "128825412477592", 
  api_secret = "ipP8mk49DeJMs_ZPDRh4uCayNyw" )

class RegisterView (APIView):

    def post(self,request):
        try:
          user = UserChat.objects.create_user(data=request.data)
          Avatar.objects.create(user=user)
          token = RefreshToken.for_user(user)
          token = {
              "refresh": str(token),
              "access": str(token.access_token)
          }
          
          return Response({
            "message": "User Created",
            "token": token,
          })
        except:
          return Response({
            "message":"Bad Request",
          },status=status.HTTP_400_BAD_REQUEST)