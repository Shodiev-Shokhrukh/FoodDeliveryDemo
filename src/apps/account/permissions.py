from rest_framework import permissions

class IsWaiterOrAdmin(permissions.BasePermission):
    message = 'You do not have the necessary permissions to perform this action.'

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # All safe methods (GET, HEAD, OPTIONS) are allowed.
            return True
        
        # Check if the user is authenticated and has the necessary role for non-safe methods.
        return request.user.is_authenticated and request.user.role in ['waiter', 'admin']

class IsWaiter(permissions.BasePermission):
    message = 'You do not have the necessary permissions to perform this action.'

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # All safe methods (GET, HEAD, OPTIONS) are allowed.
            return True
        
        # Check if the user is authenticated and has the necessary role for non-safe methods.
        return request.user.is_authenticated and request.user.role == 'waiter'