from rest_framework.views import APIView
from rest_framework.response import Response
from api.models.UserChat import UserChat
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

class RegisterView (APIView):

    def post(self,request):
        try:
          user = UserChat.objects.create_user(email=request.data['email'],last_name=request.data['last_name'],first_name=request.data['first_name'],phone=request.data['phone'],password=request.data['password'])
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
      
          