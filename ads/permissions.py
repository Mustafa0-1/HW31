from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsSelectionOwner(BasePermission):
    message = "Вы не имеете доступа к этой подборке"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False


class IsAdOwnerOrStaff(BasePermission):
    message = "Вы не имеете доступа к этой объявлению!"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author or request.user.role in [UserRoles.ADMIN, UserRoles.MODERATOR]:
            return True
        return False
