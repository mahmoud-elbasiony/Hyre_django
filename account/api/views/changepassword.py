from rest_framework.response import Response
from rest_framework import status, generics
from Landlord.models import Tenant
from Tenant.models import User
from account.api.serializers import ChangePasswordSerializer
import math
from datetime import datetime
from rest_framework.authtoken.models import Token

class ChangePasswordView(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer
    
    def put(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user=request.user
            user.set_password(serializer.validated_data.get('password'))
            user.save()
            return Response(
            {
                "success": True,
                "message": "password changed successfully",
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {
                    "status": False,
                    "message": serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
            
