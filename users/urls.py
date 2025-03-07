from django.urls import path
from .views import users_lists, add_users

urlpatterns = [
path("", users_lists, name="users_lists"),
path("add/", add_users, name="add_users"),
]