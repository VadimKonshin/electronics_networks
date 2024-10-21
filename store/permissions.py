from rest_framework import permissions


class IsActiveUserPermissions(permissions.BasePermission):
    ''' Премишин для проверки активированного пользователя '''
    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        else:
            return False
