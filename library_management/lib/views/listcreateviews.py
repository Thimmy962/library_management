from rest_framework import permissions, decorators, response, status
from ..utils import custom_permissions
from ..models import Members, Staffs
from ..utils import serializers



@decorators.api_view(["GET"])
@decorators.permission_classes(custom_permissions.StaffPermissionMixins)
def get_members(request):
    members = Members.objects.all()
    serializer = serializers.GetMemberSerializer(members, many = True)
    return response.Response(serializer.data, status=status.HTTP_200_OK)


@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def post_member(request):
        data = request.data
        data["email"] = data["email"].lower()
        serializer = serializers.PostMemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({"message": "Successful"}, status=status.HTTP_201_CREATED)
        else:
            return response.Response({"error": serializer.errors, "data": serializer.data}, status=status.HTTP_400_BAD_REQUEST)


@decorators.api_view(["GET"])
@decorators.permission_classes(custom_permissions.StaffPermissionMixins)
def get_staffs(request):
    members = Staffs.objects.all()
    serializer = serializers.GetStaffSerializer(members, many = True)
    return response.Response(serializer.data, status=status.HTTP_200_OK)


@decorators.api_view(["POST"])
@decorators.permission_classes(custom_permissions.StaffPermissionMixins)
def post_staff(request):
    data = request.data
    data["email"] = data["email"].lower()
    serializer = serializers.PostStaffSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return response.Response({"message": serializer.data}, status=status.HTTP_201_CREATED)
    else:
        return response.Response({"error": serializer.errors, "data": serializer.data}, status=status.HTTP_400_BAD_REQUEST)
