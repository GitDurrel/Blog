from django.urls import path
from .views import users_lists, add_users

urlpatterns = [
path("users/", users_lists, name="users_lists"),
path("users/", add_users, name="add_users")
]