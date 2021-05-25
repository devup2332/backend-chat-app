from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from chatProject.settings import pusher_client


class LogOutView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self,request):
        user = request.user
        user.status = False
        user.save()
        pusher_client.trigger('chat','logout-user',{
                "message": "User is logout"
        })
        return Response("You are logout")