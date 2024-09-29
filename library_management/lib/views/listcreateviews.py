from rest_framework.filters import SearchFilter, OrderingFilter
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
            return serializers.GetMemberSerializer  # Serializer for GET requests
        return serializers.PostMemberSerializer  # Default to POST serializer


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
    
    # def perform_create(self, serializer):
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return response.Response({"message": "Librarian created successfully"}, status=status.HTTP_201_CREATED)

list_create_librarian = LibrarianListCreateView.as_view()



class GenreListCreateView(custom_permissions.IsStaffOrReadOnlyMixin, generics.ListCreateAPIView):
    queryset = Genres.objects.all()  # Define the queryset
    serializer_class = serializers.GenreSerializer  # Define the serializer
    
    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return response.Response({"message": "Genre created successfully"}, status=status.HTTP_201_CREATED)

# Create an instance of the view
list_create_genres = GenreListCreateView.as_view()



class AuthorListCreateView(custom_permissions.IsStaffOrReadOnlyMixin, generics.ListCreateAPIView):
    queryset = Authors.objects.all()
    serializer_class = serializers.AuthorSerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return response.Response({"message": "Author created successfully"}, status=status.HTTP_201_CREATED)



list_create_authors = AuthorListCreateView.as_view()



# must be a staff or read only
class BooksListCreateView(custom_permissions.IsStaffOrReadOnlyMixin, generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = serializers.BookSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['book_name']  # Specify fields to search on
    ordering_fields = ['book_name']  # Fields to order by
    ordering = ['book_name'] 

    def perform_create(self, serializer):
            # Get author and genre lists from the request
            author_list = self.request.data.get("authors", [])
            genre_list = self.request.data.get("genres", [])

            # Save the book instance using validated data
            new_book = serializer.save()

            # Add genres and authors to the book
            for genre_id in genre_list:
                genre = Genres.objects.get(pk=genre_id)
                new_book.genres.add(genre)

            for author_id in author_list:
                author = Authors.objects.get(pk=author_id)
                new_book.authors.add(author)

    def create(self, request, *args, **kwargs):
            # You don't need to override this unless you want to change the response
            super().create(request, *args, **kwargs)
            return response.Response({"message": "Book created successfully"}, status=status.HTTP_201_CREATED)    
list_create_books = BooksListCreateView.as_view()
