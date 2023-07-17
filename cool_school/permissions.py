from rest_framework.permissions import BasePermission


class UserOrStuff(BasePermission):

    def has_permission(self, request, view):
        if request.user == view.get_object().user:
            return True
        elif request.user.is_staff:
            return True
        return False
