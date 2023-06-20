from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes, permission_classes, authentication_classes
from rest_framework.parsers import MultiPartParser
from Tenant.models.user import User
from rest_framework import status
from Tenant.api.serializers import GetUserSerializer
from django.views.decorators.csrf import csrf_exempt
from Tenant.api.token import createToken,verifyToken
import os
from rest_framework.exceptions import ValidationError
@api_view(["DELETE"])
@csrf_exempt
def destroy_user(request, pk):
    print(pk)
    try:
        user = User.objects.get(pk=pk)
        user.delete()
        return Response({
            "success": True,
            "message": "user deleted successfully",
        }, status=status.HTTP_201_CREATED)
    except User.DoesNotExist:
        return Response({
            "success": False,
            "message": "user does not exist",
        }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(e)
        return Response({
            "success": False,
            "message": "Server error",
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
