from django.core.mail import send_mail
# import os
# from dotenv import load_dotenv

# load_dotenv()
class RejectEmail(send_mail):
    subject = 'rejection email'
    message = 'This is the body of the rejection email.'
    # from_email = os.get("EMAIL_HOST_USER")
    from_email = "mahmoud.elbasiony904@gmail.com"
    recipient_list = ['midoking904@gmail.com']
    @classmethod
    def send_mail_message(cls):
        send_mail(cls.subject, cls.message, cls.from_email, cls.recipient_list)


