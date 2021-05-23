from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

class RefreshTokenView (APIView):

    def post(self,request):
        user = request.user
        token = RefreshToken.for_user(user)
        token = {
              "refresh": str(token),
              "access": str(token.access_token)
          }
        return Response(token)