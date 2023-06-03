from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path('add_post/', views.add_post, name='add_post'),
    path("", views.home, name = "home"),
    path("post_details/<post_id>/", views.post_details, name="post_details"),
    path("post_update/<post_id>/", views.update_post, name="update_post"),
    path("delete/<post_id>", views.delete_post, name="delete_post"),
    path("search/", views.search, name="search"),
]