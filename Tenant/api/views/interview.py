from rest_framework.response import Response
from rest_framework import status, generics
from Tenant.models import Interview, Applicant, User
from Tenant.api.serializers import InterviewSerializer , GetInterviewSerializer
from datetime import datetime
from .mail import MailView
from django.conf import settings 
import uuid


class InterviewView(generics.GenericAPIView):
    get_serializer_class = GetInterviewSerializer
    serializer_class = InterviewSerializer

    def get(self, request):
        interviews = Interview.objects.filter(company=request.user.company.id)
        serializer = self.get_serializer_class(interviews, many=True)
        return Response({
            "success": True,
            "message": "interviews retrieved successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        interview = request.data
        interview["interviewer"] = request.user.id
        interview["company"] = request.user.company_id
        room = str(uuid.uuid4())
        interview["room"] = room
        applicant = Applicant.objects.get(pk=interview["applicant"]) 
        applicant.hasInterview = True
        applicant.save()
        serializer = self.serializer_class(data=interview)
        if serializer.is_valid():
            interview = serializer.save()
            print(interview)

            applicant_data = Applicant.objects.get(
                id=int(serializer.data.get('applicant'))
            )
            interviewer_data = User.objects.get(
                id=int(serializer.data.get('interviewer'))
            )

            MailView.InterviewEmail(
                applicant_data.name,
                interviewer_data.email,
                [applicant_data.email],
                serializer.validated_data['date'],
                serializer.validated_data['room'],
                settings.MEETING_URL
                
            )

            return Response(
                {
                    "success": True,
                    "message": "interview created successfully",
                    "data":
                    {
                        "interview": serializer.data
                    }
                }, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(
                {
                    "status": False,
                    "message": serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)


class InterviewDetailView(generics.GenericAPIView):
    serializer_class = InterviewSerializer

    def get_Interview(self, pk, company):
        try:
            return Interview.objects.get(pk=pk, company=company)
        except:
            return None

    def get(self, request, pk):
        interview = self.get_Interview(pk=pk, company=request.user.company.id)
        if interview == None:
            return Response(
                {
                    "status": False,
                    "message": "Interview not found"
                }, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(interview)
        return Response({
            "status": True,
            "message": "Interview retrieved successfully",
            "data":
            {
                "interview": serializer.data
            }
        })

    def patch(self, request, pk):
        interview = self.get_Interview(pk=pk, company=request.user.company.id)
        if interview == None:
            return Response(
                {
                    "status": False,
                    "message": f"Interview with Id: {pk} not found"
                }, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            interview, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updated_at'] = datetime.now()
            serializer.save()

            applicant_data = Applicant.objects.get(
                id=int(serializer.data.get('applicant'))
            )
            interviewer_data = User.objects.get(
                id=int(serializer.data.get('interviewer'))
            )

            MailView.InterviewEmail(
                applicant_data.name,
                interviewer_data.email,
                [applicant_data.email],
                serializer.validated_data['date'],
            )

            return Response({
                "success": True,
                "message": "Interview updated successfully",
                "data":
                {
                    "interview": serializer.data
                }
            })
        return Response({
            "success": False,
            "message": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        interview = self.get_Interview(pk=pk, company=request.user.company.id)
        if interview == None:
            return Response(
                {
                    "success": False,
                    "message": f"Interview with Id: {pk} not found"
                }, status=status.HTTP_404_NOT_FOUND)

        interview.delete()
        remaining_interviews = Interview.objects.filter(
            company=request.user.company.id)
        serializer = self.serializer_class(
            remaining_interviews, many=True)

        return Response({
            "success": True,
            "message": "Interview deleted successfully",
            "data": serializer.data

        }, status=status.HTTP_200_OK)
