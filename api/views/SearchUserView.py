from api.models.User import User
from api.views.GetChat import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from api.serializers.UserSerializer import UserSerializer

class SearchUserView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(solf,request):

        words = request.data['search']

        

        if len(words) == 1:
            users = User.objects.filter(first_name__icontains=words[0]).all() | User.objects.filter(last_name__icontains=words[0]).all()
        else:
            users = User.objects.filter(first_name__icontains=words[0]).all() & User.objects.filter(last_name__icontains=words[1]).all()
                
                
        
        

        users = UserSerializer(users,many=True)

        return Response(users.data)