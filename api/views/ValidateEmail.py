from rest_framework.response import Response
from rest_framework.views import APIView
from api.models.UserChat import UserChat

class ValidateEmailView(APIView):

    def get(self,request,email):
        print(email)
        user:UserChat = UserChat.objects.filter(email=email).first()
        print(user)
        if user:
            return Response({
                "status": False,
                "message": "Email already exist"
            })
        return Response({
            "status": True,
            "message": "Email is valid to use"
        })

