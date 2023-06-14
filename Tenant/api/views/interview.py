from rest_framework.response import Response
from rest_framework import status, generics
from Tenant.models import Interview
from Tenant.api.serializers import InterviewSerializer
import math
from datetime import datetime


class InterviewView(generics.GenericAPIView):
    serializer_class = InterviewSerializer
    queryset = Interview.objects.all()

    def get(self, request):
        interviews = Interview.objects.all()
        serializer = self.serializer_class(interviews, many=True)
        return Response({
            "success": True,
            "message": "interviews retreived successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
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
            return Response(
                {
                    "status": False,
                    "message": serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)


class InterviewDetailView(generics.GenericAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer

    def get_Interview(self, pk):
        try:
            return Interview.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        interview = self.get_Interview(pk=pk)
        if interview == None:
            return Response(
                {
                    "status": False,
                    "message": f"Interview with Id: {pk} not found"
                }, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(interview)
        return Response({
            "status": True,
            "message": "Interviwe retreived successfully",
            "data":
            {
                "interview": serializer.data
            }
        })

    def patch(self, request, pk):
        interview = self.get_Interview(pk)
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
        interview = self.get_Interview(pk)
        if interview == None:
            return Response(
                {
                    "success": False,
                    "message": f"Interview with Id: {pk} not found"
                }, status=status.HTTP_404_NOT_FOUND)

        interview.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
