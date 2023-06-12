from django.db import models
from django.db import models

# Create your models here.
class Applicant(models.Model):
    gender_choice = (
  ("Male", "Male"),
  ("Female", "Female"),
)
    name = models.CharField(max_length=100,null=False)
    email= models.EmailField(null=False)
    mobile = models.CharField(max_length=128 ,null=False)
    gender = models.CharField(choices=gender_choice,null=False)
    edu_degree = models.CharField(max_length=128,null=False)
    birth_date = models.DateField(null=False)
    Resume = models.FileField(null=True)

    
    def __str__(self) -> str:
        return f"{self.name}"
