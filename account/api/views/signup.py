from rest_framework.response import Response
from django.contrib.auth.models import Group
from rest_framework import status, generics
from Tenant.models import User
from account.api.serializers import TenantSerializer
from account.api.serializers import SignupSerializer


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
                tenant_admin_group=Group.objects.filter(name="Tenant Admin").first()
                myuser=User.objects.filter(email=user.validated_data["email"]).first()
                myuser.groups.add(tenant_admin_group)
                return Response(
                    {
                        "success": True,
                        "message": "signup successfully",
                        "data":
                        {
                            "company": tenant.data
                        }
                    }, status=status.HTTP_201_CREATED)
            

