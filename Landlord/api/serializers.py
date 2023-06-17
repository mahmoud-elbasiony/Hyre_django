from rest_framework import serializers
from Landlord.models import Subscription



    
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['type',"price","name","description"]



