from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),

    path("home/", views.index, name="home"),
    path("add/", views.add_book, name="add"),
    path("search/",views.search,name="search"),

    path("user/register/", views.register, name="register"),
    path("user/login/",views.login_, name="login"),
    path("user/profile/", views.profile, name="profile"),

    path("info/<str:id>/", views.info, name="info"),
    path("info/like/<str:book_id>/", views.like_book, name="like_book"),
    path("user/profile/shelf/new/<str:name>", views.add_shelf, name="add_shelf") ,
    path("user/profile/shelf/delete/<str:shelf_id>", views.delete_shelf, name="delete_shelf") ,
    path("user/profile/shelf/add/<str:book_id>", views.add_to_shelf, name="add_to_list"),
    path("user/profile/reviews/add/<str:book_id>",views.add_review,name="add_review"),
    path("user/profile/edit/",views.edit,name="edit_profile"),  
    path("user/profile/settings/",views.settings,name="settings"),

]
