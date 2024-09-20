from django.urls import path
from .views import listcreateviews, views

urlpatterns =[
    path("", views.path_list),
    path("members/", listcreateviews.list_create_members),
    path("staffs/", listcreateviews.list_create_staffs),
    path("librarian/", listcreateviews.list_create_librarian),
    path("genres/", listcreateviews.list_create_genres),
    path("authors/", listcreateviews.list_create_authors)
]