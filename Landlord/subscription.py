from django.db import models


# Create your models here.

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Subscription(TimeStampedModel):
    name = models.CharField(max_length=100,blank=False)
    annual_price= models.FloatField(null=False)
    monthly_price= models.FloatField(null=False)
    description = models.TextField(blank=False,max_length=128)

    def __str__(self) -> str:
        return f"{self.name}"