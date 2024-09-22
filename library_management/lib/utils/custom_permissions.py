from rest_framework import permissions


# class IsSuperUser(permissions.BasePermission):
#     def has_permission(self, request, view):
#         user = request.user
#         if not bool(user.is_authenticated and user.is_superuser and user.is_active):
#             return False
#         return super().has_pemission(request, view)

# class IsStaffUser(permissions.BasePermission):
#     def has_permission(self, request, view):
#         user = request.user
#         if not bool(user and user.is_authenticated and user.is_staff):
#             return False
#         return super().has_pemission(request, view)

                # OR
"""
Custom permissions
"""

class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return bool(user.is_authenticated and user.is_superuser and user.is_active and user.is_staff)

class IsStaffUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated and is a staff member
        if request.user.is_authenticated and request.user.is_staff:
            return True
        return False

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.email == request.user.email
    

# allow any user to get but staffs alone to edit
class IsStaffOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_staff
    

"""
Custom functions
"""

def clean_data(data):
    if "email" in data:
        data["email"] = data["email"].lower()
    if "first_name" in data:
        data["first_name"] = data["first_name"].title()
    if "last_name" in data:
        data["last_name"] = data["last_name"].title()
    if "name" in data:
        data["name"] = data["name"].title()
    return data

"""
Custom mixins
"""

class IsStaffMixin:
    permission_classes = [permissions.IsAuthenticated, IsStaffUser]

class IsSuperUserMixin:
    permission_classes = [permissions.IsAuthenticated, IsSuperUser]

class IsOwnerPermissionMixinxs:
    permission_classes = [IsStaffUser, IsOwner]

class IsStaffOrReadOnlyMixin:
    permission_classes = [IsStaffOrReadOnly]