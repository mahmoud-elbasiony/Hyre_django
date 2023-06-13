from django.db import models
from Landlord.models import TimeStampedModel
from django.db import models
from .user import User
from .applicant import Applicant
from .position import Position
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Interview(TimeStampedModel):
    interviewer = models.ForeignKey(User,on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant,on_delete=models.CASCADE)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
    grade = models.IntegerField(blank=True,validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    date = models.DateField(blank=False)
    url = models.CharField(blank=False)

    
    def __str__(self) -> str:
        return f"applicant: {self.applicant} position: {self.position}"
