from Tenant.api.serializers import PositionSerializer
from Tenant.models import Position
from rest_framework.response import Response
from rest_framework import status, generics
from datetime import datetime
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt







class PositionView(generics.GenericAPIView):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()

    def get(self, request):
        positions = Position.objects.filter(company=request.user.company_id)
        print(request.user.company_id)
        serializer = self.serializer_class(positions, many=True)
        return Response({
            "success": True,
            "message": "positions retreived successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "message": "position created successfully",
                    "data":
                    {
                        "position": serializer.data
                    }
                }, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {
                    "status": False,
                    "message": serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)



class PositionDetailView(generics.GenericAPIView):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()


    def get_position(self, id):
        try:
            return Position.objects.get(pk=id)
        except:
            return None

    def get(self, request, id):
        position = self.get_position(id)
        if position == None:
            return Response(
                {
                    "status": False,
                    "message": f"position with Id: {id} not found"
                }, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(position)
        return Response({
            "status": True,
            "message": "position retreived successfully",
            "data":
            {
                "position": serializer.data
            }
        })

    def patch(self, request, id):
        position = self.get_position(id)
        if position == None:
            return Response(
                {
                    "status": False,
                    "message": f"position with Id: {id} not found"
                }, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(position, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True,
                "message": "position updated successfully",
                "data":
                {
                    "position": serializer.data
                }
            })
        return Response({
            "success": False,
            "message": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        position = self.get_position(id)
        if position == None:
            return Response(
                {
                    "success": False,
                    "message": f"position with Id: {id} not found"
                }, status=status.HTTP_404_NOT_FOUND)

        position.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
