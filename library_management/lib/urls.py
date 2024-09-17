from django.urls import path
from .views import listcreateviews, views

urlpatterns =[
    path("", views.path_list),
    path("get_members/", listcreateviews.get_members),
    path("post_member/", listcreateviews.post_member),
    path("get_staffs/", listcreateviews.get_staffs),
    path("post_staff/", listcreateviews.post_staff)
]