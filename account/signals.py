from django.db.models.signals import post_save
from django.dispatch import receiver

from Tenant.models.user import User

# from .models import CustomToken
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def user_created_handler(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)