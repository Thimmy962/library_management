

from rest_framework import permissions, decorators, response, status, views, generics
from ..utils import custom_permissions
from ..models import Members, Staffs, Librarian, Genres
from ..utils import serializers

@decorators.api_view(["GET","POST"])
def list_create_member(request):
    if request.method == "GET":
        permission = custom_permissions.IsStaffUser()
        if not permission.has_permission(request, None):
            return response.Response({"error": "You are not authorized to view member list"}, status=status.HTTP_403_FORBIDDEN)
        members = Members.objects.all()
        serializer = serializers.GetMemberSerializer(members, many=True)
        return response.Response(serializer.data)
    
    elif request.method == "POST":
        permission = permissions.AllowAny()
        if not permission.has_permission(request, None):
            return response.Response({"error": "You are not authorized to perform this action"}, status=status.HTTP_403_FORBIDDEN)
        data = request.data
        data = custom_permissions.clean_data(data)
        serializer = serializers.PostMemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({"message": "Successful"}, status=status.HTTP_201_CREATED)
        else:
            return response.Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



@decorators.api_view(["GET", "POST"])
@decorators.permission_classes([custom_permissions.IsStaffUser])
def list_create_staffs(request):
    if request.method == "GET":
        try:
            librarian = Staffs.objects.all()
            serializer = serializers.GetStaffSerializer(librarian, many=True)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return response.Response(serializer.errors)
    
    elif request.method == "POST":
        # POST request logic  # Assuming a permission check for staff
        data = custom_permissions.clean_data(request.data)
        serializer = serializers.PostStaffSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({"message": serializer.data}, status=status.HTTP_201_CREATED)
        return response.Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



@decorators.api_view(["GET", "POST"])
@decorators.permission_classes([custom_permissions.IsSuperUser])
def list_create_librarian(request):
    if request.method == "GET":
        try:
        # GET request logic
            librarian = Librarian.objects.all()
            serializer = serializers.GetLibrarianSerializer(librarian, many=True)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return response.Response(serializer.errors)
    
    elif request.method == "POST":
        # POST request logic  # Assuming a permission check for staff
        data = request.data
        data = custom_permissions.clean_data(data)
        print(data)
        serializer = serializers.PostLibrarianSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({"message": serializer.data}, status=status.HTTP_201_CREATED)
        return response.Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



@decorators.api_view(["GET","POST"])
def list_create_genres(request):
    if request.method == "GET":
        permission = permissions.AllowAny()
        if not permission.has_permission(request, None):
            return response.Response({"error": "You are not authorized to view member list"}, status=status.HTTP_403_FORBIDDEN)
        genres = Genres.objects.all()
        serializer = serializers.GenreSerializer(genres, many=True)
        return response.Response(serializer.data)
    
    elif request.method == "POST":
        permission = custom_permissions.IsSuperUser()
        if not permission.has_permission(request, None):
            return response.Response({"error": "You are not authorized to perform this action"}, status=status.HTTP_403_FORBIDDEN)
        data = request.data
        data = custom_permissions.clean_data(data)
        serializer = serializers.GenreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({"message": "Successful", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return response.Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)