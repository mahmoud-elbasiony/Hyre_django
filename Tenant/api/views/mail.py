# from emails import *
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from django.template.loader import render_to_string
from rest_framework.views import APIView


class MailView(APIView):
    def post(self, request,type):
        match type:
            case "reject":
                RejectEmailView().post(request)
            case "accept":
                AcceptEmailView.post(request)
            case "interview":
                InterviewEmailView.post(request)
        


class RejectEmailView(APIView):
    def post(self, request):
        subject = 'rejection email'
        message = 'We regret to inform you that your application has been rejected because Your application did not meet the required criteria.'
        # name = "mahmoud"
        end_message = "Thank you for your interest."
        from_email = "mahmoud.elbasiony904@gmail.com"
        recipient_list = ['midoking904@gmail.com', "mahmoud.elbasiony904@gmail.com"]
        html_message = render_to_string('mail.html', {'subject': subject, 'message': message, "end_message": end_message, "name": name})

        send_mail(subject, message, from_email, recipient_list, html_message=html_message)

        return Response(
            {
                "success": True,
                "message": "Mail sent"
            },
            status=status.HTTP_201_CREATED
        )
    
class AcceptEmailView(APIView):
    def post(self, request):
        subject = 'rejection email'
        message = 'We regret to inform you that your application has been rejected because Your application did not meet the required criteria.'
        name = "mahmoud"
        end_message = "Thank you for your interest."
        from_email = "mahmoud.elbasiony904@gmail.com"
        recipient_list = ['midoking904@gmail.com', "mahmoud.elbasiony904@gmail.com"]
        html_message = render_to_string('mail.html', {'subject': subject, 'message': message, "end_message": end_message, "name": name})

        send_mail(subject, message, from_email, recipient_list, html_message=html_message)

        return Response(
            {
                "success": True,
                "message": "Mail sent"
            },
            status=status.HTTP_201_CREATED
        )
    
class InterviewEmailView(APIView):
    def post(self, request):
        subject = 'Interview'
        message = 'We would like to invite you to a technical interview'
        name = "mahmoud"
        end_message = "Thank you for your interest."
        from_email = "mahmoud.elbasiony904@gmail.com"
        recipient_list = ['midoking904@gmail.com']
        html_message = render_to_string('mail.html', {'subject': subject, 'message': message, "end_message": end_message, "name": name})

        send_mail(subject, message, from_email, recipient_list, html_message=html_message)

        return Response(
            {
                "success": True,
                "message": "Mail sent"
            },
            status=status.HTTP_201_CREATED
        )