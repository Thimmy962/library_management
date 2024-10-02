from django.urls import path
from .views import listcreateviews, views, retrieveupdatedeleteviews

urlpatterns =[
    path("members/", listcreateviews.list_create_members),
    path("staffs/", listcreateviews.list_create_staffs),
    path("librarian/", listcreateviews.list_create_librarian),
    path("genres/", listcreateviews.list_create_genres),
    path("authors/", listcreateviews.list_create_authors),
    path("books/", listcreateviews.list_create_books),
    path("grps/", views.list_create_grps),
    path('grp/<int:id>', views.retrieve_update_delete_grp),
    path("perms/", views.get_perms),
    path("staff/<int:id>", retrieveupdatedeleteviews.retrieve_update_delete_staff),
    path("member/<int:id>", retrieveupdatedeleteviews.retrieve_update_delete_member),
    path("librarian/<int:id>", retrieveupdatedeleteviews.retrieve_update_delete_librarian),
    path("book/<int:id>", retrieveupdatedeleteviews.retrieve_update_delete_book)
]