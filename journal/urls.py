from django.urls import path

from journal import views


urlpatterns = [
    path("entry/", views.entry, name="entry")
]