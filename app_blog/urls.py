from django.urls import path
from . import views

app_name = "app_blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/<slug:slug>", views.post_page, name="post_page"),
]
