from django.urls import path
from .views import posts_lists, add_posts, posts_details

urlpatterns = [
path("", posts_lists, name="posts_lists"),
path("add/", add_posts, name="add_posts"),
path("<int:pk>/", posts_details, name="posts_details")
]