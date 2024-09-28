from django.contrib.auth.models import Group, Permission
from ..utils import custom_permissions, serializers
from rest_framework import decorators, status, response, permissions, generics

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
                "general": [
                    "members, staffs and librarian all inherits from  customuser which has the attributes below: ",
                    "email(unique) compulsory",
                    "phone_number(unique) compulsory",
                    "first_name(case insensitive) can be null",
                    "last_name(case insensitive) can be null",
                    "is_active(has a default but can be overrwritten)",
                    "is_staff(has a default but can be overrwritten)",
                    "is_superuser(has a default but can be overrwritten)",
                    "role(has default which is not meant to be overwritten, one of the ways registered users are diffentiated from staffs)",
                    "password(which will be hashed)"
                ]
            },
            {
                "path": "books/",
                "description": "list books and creates a new book",
                "permissions": "members have read only while staffs have all permissions",
                "requirement": [
                    "book_name(case insensitive)",
                    "authors(list of author id) has ManyToManyRel with authors",
                    "gneres(list of genre id) has ManyToManyRel with genres",
                    "synopsis has a default value (default = synopsis not given)"
                ]
            },
            {
                "path": "genres/",
                "description": "list books and creates a new book: Requires genre name to create a new genre, must be authenticated as, atleast librarian",
                "permissions": "authenticated and must be at leaststaff",
                "requirements": ["name(unique, case insensitive)"]
            },
            {
                "path": "authors/",
                "description": "list and creates an author: requires first_name, last_name",
                "permissions": "authenticated and must be at least staff",
                "requiremnts": "inherits from customuser"
            },
            {
                "path": "members/",
                "description": "list and creates a member: requires email and username",
                "permissions": "list members requires authentication and IsStaff(only a staff can see every library user), while anybody can create a member(library user) model",
                "requiremnts": "inherits from customuser"

            },
            {
                "path": "librarian/",
                "description": "list and creates librarian, a superuser",
                "permissions": "Must be a superuser",
                "requiremnts": "inherits from customuser"

            },
            {
                "path": "grps/",
                "description": "list and creates list and creats grps",
                "permissions": "Must be a staff"
            },
            {
                "path": "staffs/",
                "description": "list and creates staffs",
                "permissions": "Must be a staff",
                "requiremnts": "inherits from customuser"

            },
            {
                "path": "permissions/",
                "description": "list all permissions",
                "permissions": "superuser only",
                "requirements": "must be a superuser"
            },
            {
                "path": "librarian/id",
                "description": "retrieves librarian with this id and update or delete depebding on the http request",
                "permission": "superuser only",
                "requirements": "id of the librarian"
            },
            {
                "path": "staff/id",
                "description": "retrieves staff with this id and update or delete depebding on the http request",
                "permission": "superuser only",
                "requirements": "id of the staff"
            },
            {
                "path": "member/id",
                "description": "retrieves memeber with this id and update or delete depebding on the http request",
                "permission": "is staff or owner",
                "requirements": "id of the member"
            }
    ]

    return response.Response({"paths": data}, status=status.HTTP_200_OK)

#             # for groups

class GETCREATEGROUPS(custom_permissions.IsSuperUserMixin, generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer

get_create_grps = GETCREATEGROUPS.as_view()


class PermissionsListView(custom_permissions.IsStaffOrReadOnlyMixin, generics.ListCreateAPIView):
    queryset = Permission.objects.all()
    serializer_class = serializers.PermissionSerializer # Optional: restrict to logged-in users
get_perms = PermissionsListView.as_view()