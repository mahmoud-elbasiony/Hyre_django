from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes, authentication_classes
from Tenant.api.serializers import PositionSerializer
from Tenant.models import Position
from django.contrib.auth.models import AnonymousUser
from Tenant.api.token import verifyToken
from Landlord.models import Tenant
from Landlord.api.serializers import TenantSerializer
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def company_positions(request, token):
    if not isinstance(request.user,AnonymousUser):
        company_id = request.user.company_id
    else:
        payload = request.payload
        company_id = payload['company_id']
    try:
        positions = Position.objects.filter(company_id=company_id)
        serializer = PositionSerializer(positions, many=True)
        return Response({
            "success": True,
            "message": "Positions retrieved successfully",
            "data": serializer.data
        })
    except Exception as e:
        return Response({
            "success": False,
            "message": "Failed to retrieve positions",
            "data": str(e)  # Return the exception as a string
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def company_image(request, token):
    if not isinstance(request.user,AnonymousUser):
        company_id = request.user.company_id
    else:
        payload = request.payload
        company_id = payload['company_id']
    try:
        company = Tenant.objects.get(id=company_id)
        serializer = TenantSerializer(company, many=False)
        return Response({
            "success": True,
            "message": "Image retrieved successfully",
            "data": serializer.data['image']
        })
    except Exception as e:
        return Response({
            "success": False,
            "message": "Failed to retrieve company image",
            "data": str(e)  # Return the exception as a string
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Get the company data from the database
@api_view(["GET"])
def company_full_data (request):
    image=request.user.company.image.url if request.user.company.image else None
    company = {
        "name": request.user.username,
        "email": request.user.email,
        "id": request.user.id,
        "image":image,
        "company":request.user.company.name,
        "subscription":request.user.company.subscription.name
    }
    return Response ({
        "success": True,
        "message": "Retreived company successfully",
        "data": company
    },status=status.HTTP_200_OK)