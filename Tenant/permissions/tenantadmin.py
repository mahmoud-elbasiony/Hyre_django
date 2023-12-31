
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import BasePermission

class TenantAdminPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name="Tenant Admin").exists():
            return True
        return False