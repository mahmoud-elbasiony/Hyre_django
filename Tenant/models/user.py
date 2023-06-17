from django.db import models
from Landlord.models import TimeStampedModel,Tenant
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class User(AbstractUser, TimeStampedModel):
    username = models.CharField(max_length=150, unique=True, default='')
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(null=False,unique=True)
    password = models.CharField(max_length=128, blank=False)
    groups = models.ManyToManyField(
        Group,
        blank=True,
        help_text="The groups this user belongs to.",
        related_name="tenant_users"  # Add related_name argument
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="tenant_users"  # Add related_name argument
    )
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    def __str__(self):
        return f"{self.username}"
