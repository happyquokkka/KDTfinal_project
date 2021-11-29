from django.shortcuts import render

# Create your views here.
from django.urls import path
from restaurant import views as restaurant_views

app_name = "core"

urlpatterns = [path("", restaurant_views.get.as_view(), name="home")]
