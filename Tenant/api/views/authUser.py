from rest_framework.response import Response
from rest_framework import status, generics
from Tenant.models import User
from account.api.serializers import SignupSerializer
from Tenant.api.serializers import GetUserSerializer, updateUserSerializer
import math
from .mail import MailView
from Tenant.permissions import TenantAdminPermission


class AuthUserView(generics.GenericAPIView):
    serializer_class = GetUserSerializer

    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response({
            "success": True,
            "message": "user retreived successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def put(self, request):
        self.serializer_class = updateUserSerializer
        serializer = self.serializer_class(
            request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            print("putttttttttt333333333")
            return Response(
                {
                    "success": True,
                    "message": "information updated successfully",
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
                    "message": "information update failed",
                    "data": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
