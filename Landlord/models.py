from django.db import models
from .subscription import Subscription
# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
        
        
class Tenant(TimeStampedModel):
    name = models.CharField(max_length=100)
    expiration_date =  models.DateField(null=True)
    subscription= models.ForeignKey(Subscription,null=True,on_delete=models.SET_NULL)
    free_trial = models.BooleanField()
    database = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    expiration_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"

