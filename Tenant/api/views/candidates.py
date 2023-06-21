from rest_framework.response import Response
from rest_framework import status, generics
from Tenant.api.serializers import ApplicantSerializer
from Tenant.models import Applicant

class CandidateView(generics.GenericAPIView):

    serializer_class = ApplicantSerializer
    queryset = Applicant.objects.all()

    def get(self , request):

        try:
            candidates = Applicant.objects.filter(status=1)
            serializer = self.serializer_class(candidates , many=True)
            return Response({
                "success": True,
                "message": "interviews retrieved successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "success": False,
                "message": "Something Wrong Happened",
                "data": e
            }, status=status.HTTP_200_OK)
        
    def delete(self, request, pk):
        try:
            applicant = Applicant.objects.get(pk=pk)
        except Applicant.DoesNotExist:
            return Response({
                "success": False,
                "message": "Applicant not found"
            }, status=status.HTTP_404_NOT_FOUND)

        applicant.status = 2
        applicant.save()
        remaining_candidates = Applicant.objects.filter(status=1)
        serializer = self.serializer_class(remaining_candidates , many=True)
        return Response({
            "success": True,
            "message": "Applicant deleted successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
        
