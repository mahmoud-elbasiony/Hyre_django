from rest_framework.authtoken.models import Token
from Tenant.models import User
from django.db import models
# Create your models here.
# class CustomToken(models.Model):
#     token = models.OneToOneField(Token, on_delete=models.CASCADE, primary_key=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return str(self.token)
