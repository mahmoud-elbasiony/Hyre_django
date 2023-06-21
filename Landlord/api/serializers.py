from rest_framework import serializers
from Landlord.models import Subscription
from Landlord.models import Tenant


    
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['type',"price","name","description"]

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'



