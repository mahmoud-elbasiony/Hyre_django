from django.contrib.auth.models import Group
from rest_framework import serializers

from Tenant.models import Interview,Position, Applicant,User


class InterviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interview
        fields = '__all__'

class GetInterviewSerializer(serializers.ModelSerializer):
    interviewer = serializers.StringRelatedField()
    applicant = serializers.StringRelatedField()
    position = serializers.StringRelatedField()
    class Meta:
        model = Interview
        fields = '__all__'


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = '__all__'

class CandidatesSerializer(serializers.ModelSerializer):
    position = serializers.StringRelatedField()
    class Meta:
        model = Applicant
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model= Group
        fields = ('id','name')

class GetUserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    class Meta:
        model = User
        fields = ["id","name","email","company","username","groups"]

class updateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name","email"]


