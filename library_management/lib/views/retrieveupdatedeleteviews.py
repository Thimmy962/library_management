from ..models import Members, Staffs, Librarian, Books
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


class BookRetrieveUpdateDelete(custom_permissions.IsStaffOrReadOnlyMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    lookup_field = "id"
    serializer_class = serializers.BookSerializer


    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return response.Response({"message": "Librarian deleted successfully"}, status=status.HTTP_200_OK)
    
retrieve_update_delete_book = BookRetrieveUpdateDelete.as_view()
