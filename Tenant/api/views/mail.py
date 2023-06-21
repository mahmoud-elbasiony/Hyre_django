# from emails import *
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from django.template.loader import render_to_string
from rest_framework.views import APIView


class MailView(APIView):
    def post(self, request,type):
        if type=="reject":
            print("reject")
            return self.RejectEmail("mahmoud","mahmoud.elbasiony904@gmail.com",["mahmoud.elbasiony904@gmail.com"])
        elif type =="accept":
            print("accept")
            return self.AcceptEmail("mahmoud","mahmoud.elbasiony904@gmail.com",["mahmoud.elbasiony904@gmail.com"])
        elif type == "interview":
            return self.InterviewEmail("mahmoud","mahmoud.elbasiony904@gmail.com",["mahmoud.elbasiony904@gmail.com"],"https://www.google.com","2023-10-30 10:30 AM")
    @classmethod
    def RejectEmail(cls,name,from_email,recipient_list):
        subject = 'rejection email'
        message = 'We regret to inform you that your application has been rejected because Your application did not meet the required criteria.'
        end_message = "Thank you for your interest."
        html_message = render_to_string('mail.html', {'subject': subject, 'message': message, "end_message": end_message, "name": name})
        send_mail(subject, message, from_email, recipient_list, html_message=html_message)

        return Response(
            {
                "success": True,
                "message": "Mail sent"
            },
            status=status.HTTP_201_CREATED
        )
    @classmethod
    def AcceptEmail(cls,name,from_email,recipient_list):
            subject = 'acceptance email'
            message = 'Congratulations! We are pleased to inform you that your application has been accepted.'
            end_message = "Thank you for your interest and we look forward to having you onboard."
            html_message = render_to_string('mail.html', {'subject': subject, 'message': message, "end_message": end_message, "name": name})
            send_mail(subject, message, from_email, recipient_list, html_message=html_message)
            return Response(
                {
                    "success": True,
                    "message": "Mail sent"
                },
                status=status.HTTP_201_CREATED
            )
    @classmethod
    def InterviewEmail(cls,name,from_email,recipient_list,date,meeting_url=None,room="Will Be sent Before Meeting, Stay tuned"):
        subject = 'Interview'
        message = 'We would like to invite you to a technical interview'
        end_message = "Thank you for your interest."
        html_message = render_to_string('mail.html', {'subject': subject, 'message': message, "end_message": end_message, "name": name,"meeting_message":meeting_url,"date":date,"room":room})
        send_mail(subject, message, from_email, recipient_list, html_message=html_message)

        return Response(
            {
                "success": True,
                "message": "Mail sent"
            },
            status=status.HTTP_201_CREATED
        )

