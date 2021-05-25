from api.serializers.ChatSerializer import ChatSerilizer
from api.models.Chat import ChatModel
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class GetChatView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,id):
        chat = ChatModel.objects.filter(id=id).first();
        data = ChatSerilizer(chat)
        return Response(data.data)
