
from rest_framework.response import Response
from rest_framework import status, generics
from Landlord.models import Subscription
from Landlord.api.serializers import SubscriptionSerializer
import math
from datetime import datetime


class ChangeSubscriptionView(generics.GenericAPIView):
    # authentication_classes=[]
    # permission_classes=[]
  
    serializer_class = SubscriptionSerializer 

    def put(self, request):
        subscription = Subscription.objects.filter(id=request.data["subscription"]).first()
        if subscription:
            print(request.user.company)
            company= request.user.company
            company.subscription_id=subscription.id
            company.save()
            return Response({
                "success": True,
                "message": "subscription upadted successfully",
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "success": False,
                "message": "subscription upadted failed",
            }, status=status.HTTP_304_NOT_MODIFIED)

