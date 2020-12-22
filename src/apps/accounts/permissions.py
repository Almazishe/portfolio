from rest_framework import permissions


class IsSelfOrAdminOrReadOnly(permissions.BasePermission):
    """
        User permission which allows only user edit it's own data.
        Others only can read it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(obj == request.user or request.user.is_superuser)


class IsSelfOrAdmin(permissions.BasePermission):
    """
        User permission which allows only user edit it's own data.
        Others only can read it.
    """

    def has_object_permission(self, request, view, obj):
        return bool(obj == request.user or request.user.is_superuser)
