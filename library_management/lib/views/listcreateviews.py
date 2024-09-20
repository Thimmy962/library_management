
from rest_framework import permissions, decorators, response, status, generics
from ..utils import custom_permissions
from ..models import Members, Staffs, Librarian, Genres, Authors
from ..utils import serializers


class MemberListCreateView(custom_permissions.StaffMixins, generics.ListCreateAPIView):
    queryset = Members.objects.all()
    serializer_class = serializers.PostMemberSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.AllowAny()]  # Allow anyone to POST
        return super().get_permissions()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializers.GetLibrarianSerializer  # Serializer for GET requests
        return serializers.PostMemberSerializer  # Default to POST serializer

    def perform_create(self, serializer):
        cleaned_data = serializer.clean_data(self.request.data)  # Assuming custom clean_data method
        validated_serializer = self.get_serializer(data=cleaned_data)  # Pass the cleaned data to the serializer
        validated_serializer.is_valid(raise_exception=True)  # Validate the cleaned data
        validated_serializer.save()  # Save the validated data
    # Save the cleaned data directly

    def create(self, request, *args, **kwargs):
        res = super().create(request, *args, **kwargs)
        return response.Response({"message": "New member created successfully"}, status=status.HTTP_201_CREATED)

list_create_members = MemberListCreateView.as_view()

    


class StaffListCreateView(custom_permissions.StaffMixins, generics.ListCreateAPIView):
    queryset = Staffs.objects.all()  # Define the queryset
    serializer_class = serializers.PostStaffSerializer  # Default serializer for POST

    # Dynamically choose the serializer based on the request method
    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializers.GetStaffSerializer  # Serializer for GET
        return super().get_serializer_class()  # Default behavior for other methods
    
    def perform_create(self, serializer):
        # Access clean_data method within the serializer
        cleaned_data = serializer.clean_data(self.request.data)  # Call clean_data from serializer
        validated_serializer = self.get_serializer(data=cleaned_data)
        if validated_serializer.is_valid():
            validated_serializer.save()  # Save the data if valid
        else:
            raise serializers.serializers.ValidationError(validated_serializer.errors)


    def create(self, request,*args, **kwargs):
        super().create(request,*args, **kwargs)
        return response.Response({"message": "New genre created successfully"}, status=status.HTTP_201_CREATED)


list_create_staffs = StaffListCreateView.as_view()

class LibrarianListCreateView(custom_permissions.SuperUserMixins, generics.ListCreateAPIView):
    queryset = Librarian.objects.all()  # Define the queryset
    serializer_class = serializers.PostLibrarianSerializer  # Default serializer for POST

    # Dynamically choose the serializer based on the request method
    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializers.GetLibrarianSerializer  # Serializer for GET
        return super().get_serializer_class()  # Default behavior for other methods
    
    def perform_create(self, serializer):
        # Access clean_data method within the serializer
        cleaned_data = serializer.clean_data(self.request.data)  # Call clean_data from serializer
        validated_serializer = self.get_serializer(data=cleaned_data)
        if validated_serializer.is_valid():
            validated_serializer.save()  # Save the data if valid
        else:
            raise serializers.serializers.ValidationError(validated_serializer.errors)


    def create(self, request,*args, **kwargs):
        super().create(request,*args, **kwargs)
        return response.Response({"message": "New genre created successfully"}, status=status.HTTP_201_CREATED)


list_create_librarian = LibrarianListCreateView.as_view()



class GenreListCreateView(custom_permissions.StaffMixins, generics.ListCreateAPIView):
    queryset = Genres.objects.all()  # Define the queryset
    serializer_class = serializers.GenreSerializer  # Define the serializer


    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        return super().get_permissions()

    # Overriding the POST behavior for custom data cleaning
    def perform_create(self, serializer):
        # Access clean_data method within the serializer
        cleaned_data = serializer.clean_data(self.request.data)  # Call clean_data from serializer
        validated_serializer = self.get_serializer(data=cleaned_data)
        if validated_serializer.is_valid():
            validated_serializer.save()  # Save the data if valid
        else:
            raise serializers.serializers.ValidationError(validated_serializer.errors)

    # Overriding the response for POST
    def create(self, request, *args, **kwargs):
            res = super().create(request, *args, **kwargs)
            return response.Response({"message": "New genre created successfully"}, status=status.HTTP_201_CREATED)


# Create an instance of the view
list_create_genres = GenreListCreateView.as_view()


class AuthorListCreateView(custom_permissions.StaffMixins, generics.ListCreateAPIView):
    queryset = Authors.objects.all()
    serializer_class = serializers.AuthorSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        return super().get_permissions()
    
    def perform_create(self, serializer):
        cleaned_data = serializer.clean_data(self.request.data)  # Call clean_data from serializer
        validated_serializer = self.get_serializer(data=cleaned_data)
        if validated_serializer.is_valid():
            validated_serializer.save()  # Save the data if valid
        else:
            raise serializers.serializers.ValidationError(validated_serializer.errors)
    
    def create(self, request, *args, **kwargs):
        res = super().create(request, *args, **kwargs)
        return response.Response({"message": "New author created successfully"}, status=status.HTTP_201_CREATED)
    
list_create_authors = AuthorListCreateView.as_view()

