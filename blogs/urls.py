from django.urls import path

from . import views

urlpatterns = [
    # path("home", views.home, name="home"),
    path("", views.blog, name="artcles"),
    # path("article", views.article, name="article"),
]