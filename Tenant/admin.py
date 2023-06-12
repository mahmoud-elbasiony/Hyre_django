from django.contrib import admin
from .models.applicant import Applicant
from .models.interview import Interview
from .models.position import Position
from .models.user import User
# Register your models here.

admin.site.register(User)
admin.site.register(Applicant)
admin.site.register(Interview)
admin.site.register(Position)