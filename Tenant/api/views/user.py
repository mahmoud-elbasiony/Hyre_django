from rest_framework.response import Response
from rest_framework import status, generics
from Tenant.models import User
from account.api.serializers import SignupSerializer
from Tenant.api.serializers import GetUserSerializer
import math
from .mail import MailView
from Tenant.permissions import TenantAdminPermission

class UserView(generics.GenericAPIView):
    serializer_class = GetUserSerializer
    permission_classes=[TenantAdminPermission]
    def get(self, request):
        company_id=request.user.company_id
        users = User.objects.filter(company=company_id)
        serializer = self.serializer_class(users, many=True)
        return Response({
            "success": True,
            "message": "users retreived successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
            self.serializer_class = SignupSerializer
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.validated_data["company_id"]=request.user.company
                serializer.save()
                return Response(
                    {
                        "success": True,
                        "message": "user created successfully",
                        "data": {
                            "user": serializer.data
                        }
                    },
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {
                        "status": False,
                        "message": "failed to created successfully",
                        "data":serializer.errors
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )