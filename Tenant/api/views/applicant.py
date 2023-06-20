from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes, permission_classes, authentication_classes
from rest_framework.parsers import MultiPartParser
from Tenant.models.applicant import Applicant
from rest_framework import status
from Tenant.api.serializers import ApplicantSerializer
from django.views.decorators.csrf import csrf_exempt
from Tenant.api.token import createToken,verifyToken
import os
from rest_framework.exceptions import ValidationError
@api_view(['GET'])
def index (request):
    try:
        applicants = Applicant.objects.filter(company_id=request.user.id)
        serializer = ApplicantSerializer(applicants, many=True)
        return Response({
            "success": True,
            "message": "Applicants retreived successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "success": False,
            "message": "Server error"
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["GET"])
def show (request , pk):
    try:
        applicant = Applicant.objects.filter(pk=pk , company_id=request.user.id)
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
        print(e)
        return Response({
            "success": False,
            "message": "Server error"
        } , status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
@csrf_exempt
@parser_classes([MultiPartParser])
@authentication_classes([])
@permission_classes([])
def store (request , token):
    payload = request.payload
    additional_data = {
        "company": payload['company_id']
    }
    data = {**request.data.dict(), **additional_data}
    try:
        resume_file = request.FILES.get("resume")  # Retrieve the file object using the correct field name
        data["resume"] = resume_file
        serializer = ApplicantSerializer(data=data)
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
        print(e)
        return Response({
            "success": False,
            "message": "Server error"
        } , status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def show_by_position (request, position_id):
    try:
        applicant = Applicant.objects.filter(position_id=position_id, company_id=request.user.id)
        serializer = ApplicantSerializer(applicant , many=True)
        return Response ({
            "success": True,
            "message": "Applicant retreived successfully",
            "data": serializer.data
        })
    except Applicant.DoesNotExist as e:
        return Response({
            "success": True,
            "message": "There is no applicants for this position"
        }, status=status.HTTP_200_OK)
    except Exception as e :
        print(e)
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
        print(e)
        return Response({
            "success": False,
            "message": "Server error"
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
def destroy(request, pk):
    try:
        applicant = Applicant.objects.get(pk=pk)
        applicant.delete()
        return Response({
            "success": True,
            "message": "Applicant deleted successfully",
        }, status=status.HTTP_201_CREATED)
    except Applicant.DoesNotExist:
        return Response({
            "success": False,
            "message": "Applicant does not exist",
        }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(e)
        return Response({
            "success": False,
            "message": "Server error",
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def generateAplicantFormLink (request):
    token = createToken (request.user.id)
    link= f"{os.getenv('HOST')}applicants/create/{token}"
    return Response({
        "success": True,
        "message": "Token generated",
        "data" : link
    }, status=status.HTTP_200_OK)


