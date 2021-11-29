from django.core import paginator
from django.db.models.fields import DateField
from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from django.http import HttpResponse, response
from django.core.paginator import Paginator
from . import models, recommend, forms
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import json

import restaurant


class SearchView(View):

    """SearchView Definition"""

    model = models.Restaurant


class RestaurantDetail(DetailView):

    """ " Restaurant Definition"""

    model = models.Restaurant


def GetGPS(request):
    if request.method == "GET":
        latitude = request.GET.get("latitude")
        longitude = request.GET.get("longitude")
        latitude = float(latitude)
        longitude = float(longitude)
        latitude = 33.49810223975762
        longitude = 126.52499210772604
        state = [latitude, longitude]
        result = recommend.make_db(state)
        print(result)
        attractionlist = []
        for i in range(10):
            attractiondict = {
                "name": str(result["name"][i]),
                "address": str(result["address"][i]),
                "upjong": str(result["upjong"][i]),
                "OMscore": str(result["OMscore"][i]),
                "Latitude": result["Latitude"][i],
                "Longtitude": result["Longtitude"][i],
            }
            attractionlist.append(attractiondict)

        attractionJson = json.dumps(attractionlist, ensure_ascii=False)
    return render(request, "restaurant/search.html", {"attractionJson": attractionJson})


def all_restaurants(request):
    page = request.GET.get("page", 1)
    restaurant_list = attractionJson.Object.all()
    paginator = Paginator(restaurant_list, 4)
    restaurants = paginator.get_page(page)
    return render(
        request="restaurant/restaurant_list", context={"restaurants": restaurants}
    )


def get(request):
    return render(request, "home.html")
