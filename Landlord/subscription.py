from django.db import models


# Create your models here.

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True



class Subscription(TimeStampedModel):
    choice=(
        ("Annually","Annually"),
        ("Monthly","Monthly"),
    )
    name=(
        ("Bootstrap","Bootstrap"),
        ("Startup","Startup"),
        ("Business","Business"),
    )
    type= models.CharField(choices=choice,null=False)
    price= models.FloatField(null=False)
    name=models.CharField(choices=name,blank=False)
    description = models.TextField(blank=False,max_length=128,default='')
    users_no = models.IntegerField(blank=False, default=100)
    pr_id = models.CharField(blank=False , default="")

    def __str__(self) -> str:
        return f"{self.name} {self.type}"
    

