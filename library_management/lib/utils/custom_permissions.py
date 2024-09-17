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

class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user

        # if all these are true return true else return false
        return bool(user.is_authenticated and user.is_superuser and user.is_active)

class IsStaffUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated and is a staff member
        if request.user and request.user.is_authenticated and request.user.is_staff:
            return True
        return False

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.email == request.user.email

    
StaffPermissionMixins = [permissions.IsAuthenticated, IsStaffUser]


class SuperUserMixins:
    permission_classes = [permissions.IsAuthenticated, IsSuperUser]

class OwnerPermissionMixinxs:
    permission_classes = [permissions.IsAuthenticated, IsOwner]