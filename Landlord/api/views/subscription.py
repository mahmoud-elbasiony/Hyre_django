from rest_framework.response import Response
from rest_framework import status, generics
from Landlord.models import Subscription
from Landlord.api.serializers import SubscriptionSerializer
import math
from datetime import datetime


class SubscriptionView(generics.GenericAPIView):
    authentication_classes=[]
    permission_classes=[]
    serializer_class = SubscriptionSerializer 

    def get(self, request):
        subscription = Subscription.objects.all()
        serializer = self.serializer_class(subscription, many=True)
        return Response({
            "success": True,
            "message": "subscription retreived successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def get(self, request):
        subscription = Subscription.objects.all()
        serializer = self.serializer_class(subscription, many=True)
        return Response({
            "success": True,
            "message": "subscription retreived successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)





