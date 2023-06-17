from rest_framework.response import Response
from rest_framework import status, generics
from Landlord.models import Tenant
from Tenant.models import User
from account.api.serializers import SigninSerializer
import math
from datetime import datetime
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

class SigninView(generics.GenericAPIView):
    serializer_class = SigninSerializer
    authentication_classes = []
    permission_classes = []
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email=request.data["email"]
            print(email)
            user=User.objects.get(email=email)
            token, created = Token.objects.get_or_create(user=user)
            return Response(
            {
                "success": True,
                "message": "login successfully",
                "data":
                {
                    "user": {"email":serializer.data["email"]},
                    'token': token.key
                }
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {
                    "status": False,
                    "message": serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
            
  
