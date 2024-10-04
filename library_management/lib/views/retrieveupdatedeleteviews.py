from ..models import Members, Staffs, Librarian, Books, Reviews
from rest_framework import generics, response, status
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


class BookRetrieveUpdateDeleteView(custom_permissions.IsStaffOrReadOnlyMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    lookup_field = "id"
    serializer_class = serializers.BookSerializer


    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return response.Response({"message": "Book deleted successfully"}, status=status.HTTP_200_OK)
    
retrieve_update_delete_book = BookRetrieveUpdateDeleteView.as_view()


class ReviewRetrieveUpdateDeleteView(custom_permissions.IsStaffOrOwnerMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    lookup_field = "id"
    serializer_class = serializers.ReviewSerializer
    permission_classes = [custom_permissions.IsSuperUserOrOwnerOfReview]


    def update(self, request, *args, **kwargs):
        try:
            super().update(request, *args, **kwargs)
            return response.Response({"message": "Review has been updated successfully"}, status=status.HTTP_202_ACCEPTED)
        except Exception:
            return response.Response({"message": "could not modify update"})
    
    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return response.Response({"message": "Review deleted successfully"}, status=status.HTTP_200_OK)
        
retrieve_update_delete_reviews = ReviewRetrieveUpdateDeleteView.as_view()
