from django.db import models
from .subscription import Subscription
# Create your models here.

        
        
class Tenant(models.Model):
    name = models.CharField(max_length=100)
    subscription= models.ForeignKey(Subscription,null=True,on_delete=models.SET_NULL)
    free_trial = models.BooleanField()
    expiration_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"
    

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company= models.ForeignKey(Tenant,on_delete=models.CASCADE,blank=False)

    class Meta:
        abstract = True
