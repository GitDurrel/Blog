from django.urls import path
from .views import posts_lists, add_posts, posts_details

urlpatterns = [
path("posts/", posts_lists, name="posts_lists"),
path("posts/", add_posts, name="add_posts"),
path("posts/<int:pk>/", posts_details, name="posts_details")
]