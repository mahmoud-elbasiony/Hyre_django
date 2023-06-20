from rest_framework.response import Response
from rest_framework import status, generics
from Landlord.models import Tenant
from Tenant.permissions.tenantadmin import TenantAdminPermission
from cloudinary_app.api.serializers import ImageSerializer

class ImageView(generics.GenericAPIView):
    serializer_class = ImageSerializer
    permission_classes=[TenantAdminPermission]
    def put(self, request):
        company = request.user.company_id
        company = Tenant.objects.get(id=company)
        try:
            serializer = self.serializer_class(company, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "success": True,
                    "message": "Image uploaded successfully",
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "success": False,
                    "message": serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({
                "success": False,
                "message": "Server error",
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



