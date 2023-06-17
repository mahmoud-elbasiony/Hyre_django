from rest_framework import serializers
from Tenant.models import Interview,Position, Applicant



class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = '__all__'


class ApplicantSerializer(serializers.ModelSerializer):
    position = serializers.StringRelatedField() # used to return string name instead of id of position like accessors in laravel
    class Meta:
        model = Applicant
        fields = '__all__'

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'



