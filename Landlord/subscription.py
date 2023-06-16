from django.db import models


# Create your models here.

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True



class Subscription(TimeStampedModel):
    choice=(
        ("Annual","Annual"),
        ("Monthly","Monthly"),
    )
    name=(
        ("free","free"),
        ("gold","gold"),
        ("plantium","plantium"),
    )
    type= models.CharField(choices=choice,null=False)
    price= models.FloatField(null=False)
    name=models.CharField(choices=name,blank=False)
    description = models.TextField(blank=False,max_length=128,default='')

    def __str__(self) -> str:
        return f"{self.name} {self.type}"
    

