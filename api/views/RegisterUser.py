from api.serializers.AvatarSerializer import AvatarSerializer
from api.models.Avatar import Avatar
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models.User import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

class RegisterView (APIView):

    def post(self,request):
          user:User = User.objects.register(data=request.data)
          user.status = True
          user.save();
          avatar = Avatar.objects.create()
          user.avatar = avatar
          user.save()
          avatar = AvatarSerializer(avatar)
          token = RefreshToken.for_user(user)
          token = {
              "refresh": str(token),
              "access": str(token.access_token)
          }
          
          return Response({
            "message": "User Created",
            "token": token,
            "avatar": avatar.data
          })
      
          