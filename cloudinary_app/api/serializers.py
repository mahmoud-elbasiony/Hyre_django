from rest_framework import serializers

from Landlord.models import Tenant

class ImageSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        self.image = validated_data.get('image')
        # Save the image to Cloudinary storage
        instance.image = self.image
        instance.save()
        return instance
    
    class Meta:
        model = Tenant
        fields = ['image']
