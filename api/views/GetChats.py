from api.serializers.ChatSerializer import ChatSerilizer
from api.models.Chat import ChatModel
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class GetChatsView (APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):

        user = request.user
        
        chats = ChatModel.objects.filter(user_1=user) | ChatModel.objects.filter(user_2=user)
        chatSerializer = ChatSerilizer(chats,many=True)

        return Response(chatSerializer.data)