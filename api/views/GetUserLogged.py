from api.models.Chat import Chat

from api.serializers.AvatarSerializer import AvatarSerializer
from api.views.GetChats import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models.Avatar import Avatar
from rest_framework.permissions import IsAuthenticated
from api.serializers import UserSerializer
class GetUserLogged(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = request.user
        user = UserSerializer(user)
        return Response(user.data)
        