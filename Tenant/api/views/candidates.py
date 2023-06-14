from rest_framework.response import Response
from rest_framework import status, generics
from Tenant.api.serializers import CandidatesSerializer
from Tenant.models import Applicant


class CandidateView(generics.GenericAPIView):

    serializer_class = CandidatesSerializer
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
                "success": True,
                "message": "Something Wrong Happened",
                "data": e
            }, status=status.HTTP_200_OK)

        
