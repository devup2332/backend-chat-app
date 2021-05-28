from rest_framework.response import Response
from rest_framework.views import APIView
from api.models.User import User

class ValidateEmailView(APIView):

    def get(self,request,email):
        user:User = User.objects.filter(email=email).first()
        if user:
            return Response({
                "status": False,
                "message": "Email already exist"
            })
        return Response({
            "status": True,
            "message": "Email is valid to use"
        })

