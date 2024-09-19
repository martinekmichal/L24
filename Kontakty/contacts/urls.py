from django.urls import path
from .views import *

urlpatterns = [
    path("kontakt_detail/<int:pk>/", KontaktDetailView.as_view(), name="kontakt_detail"),
    path("kontakt_list/", KontaktListView.as_view(), name="kontakt_list"),
    path("kontakt_create/", KontaktCreateView.as_view(), name="kontakt_create"),
    path("kontakt_detail/<int:pk>/delete/", KontaktDeleteView.as_view(), name="kontakt_delete"),
    path("kontakt_detail/<int:pk>/edit/", KontaktUpdateView.as_view(), name="kontakt_edit"),
]