from django.urls import path
from . import views

app_name = "sights"

urlpatterns = [
    path("search/", views.search, name="search"),
    path("sights_list/", views.result2, name="sights_list"),
]
