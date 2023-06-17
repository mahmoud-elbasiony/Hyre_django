from rest_framework.response import Response
from rest_framework.decorators import api_view
from Tenant.models.applicant import Applicant
from rest_framework import status
from Tenant.api.serializers import ApplicantSerializer
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

@api_view(['GET'])
def index (request):
    try:
        applicants = Applicant.objects.all()
        serializer = ApplicantSerializer(applicants, many=True)
        return Response({
            "success": True,
            "message": "Applicants retreived successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "success": False,
            "message": "Server error"
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["GET"])
def show (request , pk):
    try:
        applicant = Applicant.objects.get(pk=pk)
        serializer = ApplicantSerializer(applicant , many=False)
        return Response ({
            "success": True,
            "message": "Applicant retreived successfully",
            "data": serializer.data
        })
    except Applicant.DoesNotExist as e:
        return Response({
            "success": False,
            "message": "Applicant does not exists"
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e :
        return Response({
            "success": False,
            "message": "Server error"
        } , status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["GET"])
def create (request):
    form_url = os.getenv('HOST') + 'applicants/create'
    return HttpResponseRedirect(form_url)

@api_view(["POST"])
@csrf_exempt
def store (request):
    try:
        serializer = ApplicantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True,
                "message": "Applicant created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response ({
            "success": False,
            "message": "Invalid inserted data",
            "data" : serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            "success": False,
            "message": "Server error"
        } , status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT", "PATCH"])
@csrf_exempt
def edit(request, pk):
    try:
        applicant = Applicant.objects.get(pk=pk)
        serializer = ApplicantSerializer(applicant, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True,
                "message": "Applicant updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            "success": False,
            "message": "Invalid data",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    except Applicant.DoesNotExist:
        return Response({
            "success": False,
            "message": "Applicant does not exist"
        }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({
            "success": False,
            "message": "Server error"
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
def destroy(request, pk):
    try:
        applicant = Applicant.objects.get(pk=pk)
        applicant.delete()
        return Response({
            "success": True,
            "message": "Applicant deleted successfully",
        }, status=status.HTTP_204_NO_CONTENT)
    except Applicant.DoesNotExist:
        return Response({
            "success": False,
            "message": "Applicant does not exist",
        }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({
            "success": False,
            "message": "Server error",
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)