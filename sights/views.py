from django.db.models.fields import DateField
from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from django.http import HttpResponse, response
from django.core.paginator import Paginator
from . import models, topic1
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


def search(request):
    return render(request, "sights/search.html")


def result2(request):
    if request.method == "GET":
        a = request.GET.get("topic")
        a1 = [a]
        result2 = topic1.make_json(a1)
        print(result2)
        attractionlist = []
        for i in range(len(result2["name"])):
            attractiondict = {
                "name": str(result2["name"][i]),
                "address": str(result2["address"][i]),
                "Latitude": result2["Latitude"][i],
                "Longitude": result2["Longitude"][i],
            }
            attractionlist.append(attractiondict)

        attractionJson = json.dumps(attractionlist, ensure_ascii=False)
    return render(
        request, "sights/sights_list.html", {"attractionJson": attractionJson}
    )
