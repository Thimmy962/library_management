import logging

logger = logging.getLogger(__name__)
from ..models import Members, Staffs, Librarian, Books, Reviews, Authors
from rest_framework import (generics, response, status, permissions)
from ..utils import serializers, custom_permissions

class MemberRetrieveUpdateDeleteView(custom_permissions.IsStaffOrOwnerMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Members.objects.all()
    lookup_field = "id"
    serializer_class = serializers.GetMemberSerializer


    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return response.Response({"message": "Member deleted successfully"}, status=status.HTTP_200_OK)

retrieve_update_delete_member = MemberRetrieveUpdateDeleteView.as_view()


class StaffRetrieveUpdateDeleteView(custom_permissions.IsSuperUserMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Staffs.objects.all()
    lookup_field = "id"
    serializer_class = serializers.GetStaffSerializer


    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return response.Response({"message": "Staff deleted successfully"}, status=status.HTTP_200_OK)

retrieve_update_delete_staff = StaffRetrieveUpdateDeleteView.as_view()


class LibrarianRetrieveUpdateDeleteView(custom_permissions.IsSuperUserMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Librarian.objects.all()
    lookup_field = "id"
    serializer_class = serializers.GetLibrarianSerializer


    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return response.Response({"message": "Librarian deleted successfully"}, status=status.HTTP_200_OK)

retrieve_update_delete_librarian = LibrarianRetrieveUpdateDeleteView.as_view()


class AuthorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Authors.objects.all()
    serializer_class = serializers.AuthorSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "id"

retrieve_update_delete_author = AuthorRetrieveUpdateDeleteView.as_view()

class BookRetrieveUpdateDeleteView(custom_permissions.IsStaffOrReadOnlyMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    lookup_field = "id"
    serializer_class = serializers.BookSerializer

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return response.Response({"message": "Book deleted successfully"}, status=status.HTTP_200_OK)
    
retrieve_update_delete_book = BookRetrieveUpdateDeleteView.as_view()


class ReviewRetrieveUpdateDeleteView(custom_permissions.IsSuperUserOrOwnerOfReviewMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    lookup_field = "id"
    serializer_class = serializers.ReviewSerializer

    def update(self, request, *args, **kwargs):
        try:
            super().update(request, *args, **kwargs)
            return response.Response({"message": "Review has been updated successfully"}, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return response.Response({"message": str(e)})
    
    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return response.Response({"message": "Review deleted successfully"}, status=status.HTTP_200_OK)
        
retrieve_update_delete_reviews = ReviewRetrieveUpdateDeleteView.as_view()
