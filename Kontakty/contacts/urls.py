from django.urls import path
from .views import *

urlpatterns = [
    path("kontakt_detail/<int:pk>/", KontaktDetailView.as_view(), name="kontakt_detail"),
    path("kontakt_list/", KontaktListView.as_view(), name="kontakt_list"),
    path("kontakt_create/", KontaktCreateView.as_view(), name="kontakt_create"),
    path("kontakt_detail/<int:pk>/delete/", KontaktDeleteView.as_view(), name="kontakt_delete"),
    path("kontakt_detail/<int:pk>/edit/", KontaktUpdateView.as_view(), name="kontakt_edit"),
    path("json/", my_json, name="json"),
    path("download/", my_file_view, name="file_view"),
    path("download_img/",my_image_view, name="img_view"),
]