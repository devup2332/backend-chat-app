from rest_framework.response import Response
from rest_framework.views import APIView
from api.models.Message import Message
from api.serializers.MessageSerializer import MessageSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser

class MessageView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]

    def get(self,request):

        query = Message.objects.all()
        serializer = MessageSerializer(query,many=True)

        return Response(serializer.data)