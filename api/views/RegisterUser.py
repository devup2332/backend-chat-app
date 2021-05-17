from rest_framework.views import APIView
from rest_framework.response import Response
from api.models.UserChat import UserChat

class RegisterView (APIView):

    def post(self,request):
        
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        phone = request.data['phone']
        password = request.data['password']
        user = UserChat.objects.create_user(email=email,first_name=first_name,last_name=last_name,phone=phone,password=password)

        
        return Response("User register successfully")