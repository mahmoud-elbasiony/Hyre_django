from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
# Create your models here.
class Subscription(TimeStampedModel):
    name = models.CharField(max_length=100,blank=False)
    annual_price= models.FloatField(null=False)
    monthly_price= models.FloatField(null=False)

    def __str__(self) -> str:
        return f"{self.name}"