from django.db import models
from Landlord.models import TimeStampedModel
from .position import Position
# Create your models here.
class Applicant(TimeStampedModel):
    gender_choice = (
  ("Male", "Male"),
  ("Female", "Female")
)
    status_choice = (
  ("Accepted", 1),
  ("Rejected", 0),
  ("Pending", 2)
)
    name = models.CharField(max_length=100,null=False)
    email= models.EmailField(null=False)
    mobile = models.CharField(max_length=128 ,null=False)
    gender = models.CharField(choices=gender_choice,null=False)
    edu_degree = models.CharField(max_length=128,null=False)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
    status = models.IntegerField(choices=status_choice,null=False)
    birth_date = models.DateField(null=False)
    Resume = models.FileField(null=True)


    def __str__(self) -> str:
        return f"{self.name}"
