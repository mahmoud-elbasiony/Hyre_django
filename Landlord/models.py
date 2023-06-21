from django.db import models
from .subscription import Subscription


class Tenant(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subscription = models.ForeignKey(
        Subscription, null=True, on_delete=models.SET_NULL)
    free_trial = models.BooleanField(default=True)
    expiration_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self) -> str:
        return f"{self.name}"


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(
        Tenant, on_delete=models.CASCADE, blank=False, default="")
    # company = models.ForeignKey(
    # Tenant, on_delete=models.SET_NULL, blank=True, null=True, default=None)

    class Meta:
        abstract = True
