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
        if request.user and request.user.is_authenticated and request.user.is_staff:
            return True
        return False

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.email == request.user.email
    
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

class StaffMixins:
    permission_classes = [permissions.IsAuthenticated, IsStaffUser]

class SuperUserMixins:
    permission_classes = [permissions.IsAuthenticated, IsSuperUser]

class OwnerPermissionMixinxs:
    permission_classes = [permissions.IsAuthenticated, IsOwner]