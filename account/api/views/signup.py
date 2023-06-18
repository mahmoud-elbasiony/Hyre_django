from rest_framework.response import Response
from rest_framework import status, generics
from Landlord.models import Tenant
from account.api.serializers import TenantSerializer
from account.api.serializers import SignupSerializer
import math
from datetime import datetime


class SignupView(generics.GenericAPIView):
    serializer_class = TenantSerializer
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        tenant = self.serializer_class(data=request.data)
        if not tenant.is_valid():
            return Response(
                {
                    "status": False,
                    "message": "signup faild",
                    "data":tenant.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            user_data=tenant.validated_data.get('user')
            user=SignupSerializer(data=user_data)
            if not user.is_valid():
                return Response(
                    {
                        "status": False,
                        "message": user.errors,
                        "data": user.errors
                    }, status=status.HTTP_400_BAD_REQUEST)
            
            else:
                tenant.save()
                user.validated_data["company_id"]=tenant.instance
                user.save()
                return Response(
                    {
                        "success": True,
                        "message": "signup successfully",
                        "data":
                        {
                            "company": tenant.data
                        }
                    }, status=status.HTTP_201_CREATED)
            

