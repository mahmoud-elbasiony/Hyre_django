from Tenant.api.token import verifyToken
from rest_framework.response import Response
from rest_framework import status

class ApplicantsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/tenant/applicants/create/') or request.path.startswith('/company/positions/'):
            token = request.path.split('/')[-1]
            payload = verifyToken(token)
            if not payload:
                return Response({
                    "success": False,
                    "message": "Form time ended. Please submit the form within the specified time."
                }, status=status.HTTP_404_NOT_FOUND)
            request.payload = payload
        response = self.get_response(request)
        return response
