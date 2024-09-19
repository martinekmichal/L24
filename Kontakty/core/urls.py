from django.urls import path
from .views import *
from django.contrib.auth import views as kontakty


urlpatterns = [
    path("", home_page, name="home"),
    path("about/", about_page, name="about"),
    path("kontakt_list/", contacts_page, name="kontakt_list"),
    path("profile/", profile_page, name="profile"),
    path('register/', register_page, name='register'),
    path('login/', kontakty.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', kontakty.LogoutView.as_view(template_name='logout.html'), name='logout'),
]