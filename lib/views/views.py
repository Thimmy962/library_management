import logging

# Create a logger instance
logger = logging.getLogger(__name__)

from rest_framework.filters import SearchFilter, OrderingFilter
from django.contrib.auth.models import Group, Permission
from ..utils import custom_permissions, serializers
from rest_framework import decorators, status, response, generics

# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView

# # JWT Configuration
# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         # Add custom claims
#         if not user.username:
#             token['name'] = user.email
#         else:
#             token['name'] = user.username
#         # ...

#         return token


#             # for groups

class GETCREATEGROUPS(custom_permissions.IsSuperUserMixin, generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ["id", "name"]
    ordering_fields = ["id", "name"]
    ordering = ["id"]


    def perform_create(self, serializer):
        logging.info("Creating new group")        
        permission_ids = self.request.data.get("permission_ids", [])
        new_grp = serializer.save()
        for permission_id in permission_ids:
            try:
                permission = Permission.objects.get(pk=permission_id)
                new_grp.permissions.add(permission)
            except Permission.DoesNotExist:
                logging.error("Permission with id {} does not exist".format(permission_id))
                continue

list_create_grps = GETCREATEGROUPS.as_view()


class RETRIEVEUPDATEDELETEGROUPS(custom_permissions.IsSuperUserMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    lookup_field = "id"

    def perform_update(self, serializer):
        # Get permissions to add and remove from the request
        logging.info("Hello World")
        permission_ids_to_add = self.request.data.get("permission_ids_to_add", [])
        permission_ids_to_remove = self.request.data.get("permission_ids_to_remove", [])


        # Save the updated group details (e.g., name change)
        updated_group = serializer.save()

        # Remove specified permissions from the group
        for permission_id in permission_ids_to_remove:
            try:
                permission = Permission.objects.get(pk=permission_id)
                updated_group.permissions.remove(permission)
            except Permission.DoesNotExist:
                continue
        
        # Add new permissions to the group
        for permission_id in permission_ids_to_add:
            try:
                permission = Permission.objects.get(pk=permission_id)
                updated_group.permissions.add(permission)
            except Permission.DoesNotExist:
                continue
        
        return response.Response({"detail": "Group updated successfully"}, status=status.HTTP_200_OK)
    

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return response.Response({"message": "Group deleted successfully"}, status=status.HTTP_200_OK)

retrieve_update_delete_grp = RETRIEVEUPDATEDELETEGROUPS.as_view()


class PermissionsListView(custom_permissions.IsStaffOrReadOnlyMixin, generics.ListCreateAPIView):
    queryset = Permission.objects.all()
    serializer_class = serializers.PermissionSerializer # Optional: restrict to logged-in users
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ["name", "codename", "content_type"]
    ordering_fields = ["name"]
    ordering = ["name"]

get_perms = PermissionsListView.as_view()