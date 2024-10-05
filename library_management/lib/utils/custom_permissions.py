from django.contrib.contenttypes.models import ContentType      
from .. import models
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
        return bool(user.is_authenticated and user.is_superuser and user.is_active)

class IsStaffUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated and is a staff member
        if request.user.is_authenticated and request.user.is_staff:
            return True
        return False

class IsMember(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        # get the content type of member
        member_content_type = ContentType.objects.get_for_model(models.Members)
        # if the user is and is a member
        return bool(user.is_authenticated and user.role == "MEMBER")


# allow any user to get but staffs alone to edit
class IsStaffOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_staff


class IsStaffOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        # Allow if the user is authenticated and is staff or the owner (by email comparison)
        return user.is_authenticated and (user.is_staff or obj.email == user.email)

# if the user is a stff or the person who wrote the review
class IsSuperUserOrOwnerOfReview(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_authenticated and user.is_superuser:
            return True
        '''
            every reviewer is member
            if the email of reviewer of this current review is the same as the email of the current user i.e the current user is also wrote this review
                return True  
        '''
        return user.email == obj.reviewer.email


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
    permission_classes = [IsStaffUser]

class IsSuperUserMixin:
    permission_classes = [IsSuperUser]

class IsStaffOrOwnerMixin:
    permission_classes = [IsStaffOrOwner]

class IsStaffOrReadOnlyMixin:
    permission_classes = [IsStaffOrReadOnly]

class IsSuperUserOrOwnerOfReviewMixin:
    permission_classes = [IsSuperUserOrOwnerOfReview]