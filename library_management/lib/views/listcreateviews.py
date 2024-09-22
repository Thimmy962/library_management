from rest_framework import permissions, response, status, generics
from ..utils import custom_permissions
from ..models import Members, Staffs, Librarian, Genres, Authors, Books
from ..utils import serializers

class MemberListCreateView(custom_permissions.IsStaffMixin, generics.ListCreateAPIView):
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
        # check if a member with this email exists
        data = self.request.data
        serializers.validate_email(data.get("email"))

        serializer = self.get_serializer(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return response.Response({"message": "Member created successfully"}, status=status.HTTP_201_CREATED)

list_create_members = MemberListCreateView.as_view()


class StaffListCreateView(custom_permissions.IsStaffMixin, generics.ListCreateAPIView):
    queryset = Staffs.objects.all()  # Define the queryset
    serializer_class = serializers.PostStaffSerializer  # Default serializer for POST

    # Dynamically choose the serializer based on the request method
    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializers.GetStaffSerializer  # Serializer for GET
        return super().get_serializer_class()  # Default behavior for other methods
    
    def perform_create(self, serializer):
        # check if a member with this email exists
        data = self.request.data
        serializers.validate_email(data.get("email"))

        serializer = self.get_serializer(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return response.Response({"message": "Staff created successfully"}, status=status.HTTP_201_CREATED)

list_create_staffs = StaffListCreateView.as_view()


# must be a superuser
class LibrarianListCreateView(custom_permissions.IsSuperUserMixin, generics.ListCreateAPIView):
    queryset = Librarian.objects.all()  # Define the queryset
    serializer_class = serializers.PostLibrarianSerializer  # Default serializer for POST

    # Dynamically choose the serializer based on the request method
    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializers.GetLibrarianSerializer  # Serializer for GET
        return super().get_serializer_class()  # Default behavior for other methods
    
    def perform_create(self, serializer):
        # check if a member with this email exists
        data = self.request.data
        serializers.validate_email(data.get("email"))

        serializer = self.get_serializer(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return response.Response({"message": "Librarian created successfully"}, status=status.HTTP_201_CREATED)

list_create_librarian = LibrarianListCreateView.as_view()



class GenreListCreateView(custom_permissions.IsStaffOrReadOnlyMixin, generics.ListCreateAPIView):
    queryset = Genres.objects.all()  # Define the queryset
    serializer_class = serializers.GenreSerializer  # Define the serializer


    def perform_create(self, serializer):
        cleaned_data = serializer.clean_data(self.request.data)  # Assuming custom clean_data method
        serializer = self.get_serializer(data=cleaned_data)
        serializer.is_valid(raise_exception=True)
        return serializer.save()
    
    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return response.Response({"message": "Genre created successfully"}, status=status.HTTP_201_CREATED)

# Create an instance of the view
list_create_genres = GenreListCreateView.as_view()



class AuthorListCreateView(custom_permissions.IsStaffOrReadOnlyMixin, generics.ListCreateAPIView):
    queryset = Authors.objects.all()
    serializer_class = serializers.AuthorSerializer


    def perform_create(self, serializer):
        cleaned_data = serializer.clean_data(self.request.data)

        # check if an author with this name exists
        if Authors.objects.filter(
            first_name = cleaned_data["first_name"], last_name = cleaned_data["last_name"]).exists():
            raise serializers.serializers.ValidationError(
                "Author with this name already exists"
            )
        
        serializer = self.get_serializer(data=cleaned_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    
    def create(self, request, *args, **kwargs):
        try:
            super().create(request, *args, **kwargs)
            return response.Response({"message": "Author created successfully"}, status=status.HTTP_201_CREATED)
        except serializers.serializers.ValidationError as e:
            return response.Response({"message": str(e.args[0])}, status=status.HTTP_400_BAD_REQUEST)
    
list_create_authors = AuthorListCreateView.as_view()



# must be a staff or read only
class BooksListCreateView(custom_permissions.IsStaffOrReadOnlyMixin, generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = serializers.BooKSerializer
    

    def perform_create(self, serializer):
        cleaned_data = serializer.clean_data(self.request.data)

        # list containing ids of all tha authors that wrote this book
        author_list = cleaned_data.get("authors")

        # list containing ids of all tha genres that this book is in
        genre_list = cleaned_data.get("genres")

        serializer = self.get_serializer(data = cleaned_data)
        if serializer.is_valid(raise_exception = True):
            new_book = serializer.save()
            new_book

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return response.Response({"message": "Book created successfully"}, status=status.HTTP_201_CREATED)
    
list_create_books = BooksListCreateView.as_view()
