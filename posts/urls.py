from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.PostsList.as_view(), name="list_view"),
    path("posts/details/<int:pk>", views.PostDetails.as_view(), name="details_view"),
    path("posts/comment/", views.PostComment.as_view(), name="comment_view"),
    path("posts/create/", views.PostCreate.as_view(), name="create_view"),
    path("posts/edit/<int:pk>", views.PostEdit.as_view(), name="edit_view"),
    path("posts/delete/<int:pk>", views.PostDelete.as_view(), name="delete_view"),
]
