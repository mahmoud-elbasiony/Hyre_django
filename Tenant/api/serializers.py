from rest_framework import serializers
from Tenant.models import Interview,Position, Applicant



class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position

class CandidatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = '__all__'
