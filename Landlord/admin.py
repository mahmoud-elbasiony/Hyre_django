from django.contrib import admin
from .subscription import Subscription
from .models import Tenant
# Register your models here.
admin.site.register(Subscription)
admin.site.register(Tenant)
