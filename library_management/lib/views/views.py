# from django.contrib.auth.models import Group, Permission
from rest_framework import decorators, status, response, permissions
# from ..utils import serializers
# from ..utils import custom_permissions

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


@decorators.api_view(["GET"])
@decorators.permission_classes([permissions.AllowAny])
def path_list(request):
    data = [
        {
            "Header": "Documentation on endpoints"
        },
        {
            "general requirement": "The following models requires at least username, password and email: [members, staffs]"
        },
        {
            "path": "books/",
            "description": "list books and creates a new book: Requires book name, description, genres(a list), authors(a list), is_boorowed(is the book borrowed)"
        },
        {
            "path": "genres/",
            "description": "list books and creates a new book: Requires genre name to create a new genre, must be authenticated as, atleast librarian",
            "permissions": "authenticated and must be at leaststaff"
        },
        {
            "path": "authors/",
            "description": "list and creates an author: requires first_name, last_name",
            "permissions": "authenticated and must be at least staff"
        },
        {
            "path": "members/",
            "description": "list and creates a member: requires email and username",
            "permissions": "list members requires authentication and IsStaff(only a staff can see every library user), while anybody can create a member(library user) model"
        },
        {
            "path": "librarian/",
            "description": "list and creates a librariann a superuser",
            "permissions": "Must be a superuser"
        },
        {
            "path": "grps/",
            "description": "list and creates list and creats grps",
            "permissions": "Must be a staff"
        },
        {
            "path": "staffs/",
            "description": "list and creates staffs",
            "permissions": "Must be a staff"
        },
        {
            "path": "permissions/",
            "description": "list",
            "permissions": "a superuser"
        }
    ]

    return response.Response({"paths": data}, status=status.HTTP_200_OK)

#             # for groups

# class GETCREATEGROUPS(custom_permissions.SuperUserMixins, generics.ListAPIView):
#     queryset = Group.objects.all()
#     serializer_class = serializers.GrpSerializer
# get_create_grps = GETCREATEGROUPS.as_view()


# class PermissionsListView(generics.ListCreateAPIView):
#     queryset = Permission.objects.all()
#     permission_classes = [permissions.AllowAny] 
#     serializer_class = serializers.PermissionSerializer # Optional: restrict to logged-in users
# get_perms = PermissionsListView.as_view()