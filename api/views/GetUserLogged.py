from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from api.models import UserChat,Avatar
from api.serializers import UserChatSerializer,AvatarSerializer

class GetUserLogged(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        
        user = UserChatSerializer(request.user)
        return Response(user.data)
        