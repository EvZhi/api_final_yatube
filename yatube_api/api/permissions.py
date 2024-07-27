from rest_framework import permissions


class AuthorPermission(permissions.BasePermission):
    message = 'Изменение/удаление чужих данных запрещено.'

    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS
            or request.user
            and request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
