from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),

    path("home/", views.index, name="home"),
    path("add/", views.add_book, name="add"),
    path("search/",views.search,name="search"),
    path("info/<str:id>/", views.info, name="info"),
    path("info/add/<str:book_id>/", views.add_to_list, name="add_to_list"),
    path("info/like/<str:book_id>/", views.like_book, name="like_book"),
    path("user/register/", views.register, name="register"),
    path("user/login/",views.login_, name="login"),
    path("user/profile/", views.profile, name="profile"),    

]
