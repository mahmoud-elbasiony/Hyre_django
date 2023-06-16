from django.db import models
from Landlord.models import TimeStampedModel

# Create your models here.
class Position(TimeStampedModel):
    name = models.CharField(max_length=100,blank=False)
    vacancies= models.IntegerField(blank=False,null=True)
    description = models.TextField(blank=False,max_length=128)
    end_date = models.DateField(blank=False)
    def __str__(self) -> str:
        return f"{self.name}"
