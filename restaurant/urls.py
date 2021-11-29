from django.urls import path
from . import views

app_name = "restaurant"

urlpatterns = [
    path("search/", views.GetGPS, name="search"),
    path("restaurant_list/", views.all_restaurants, name="restaurants_list"),
]
