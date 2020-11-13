from django.shortcuts import render, redirect
from rest_framework import viewsets
from APIsApp.serializers import RouteSerializer
from APIsApp.models import Route
from APIsApp.forms import CoordinatesForm
from .routeapi import RouteApiRequest


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

def buttonSiteView(request):
    
    if request.method == "POST":
        form = CoordinatesForm(request.POST)
        if form.is_valid():

            longitude_start = form.cleaned_data['longitude_start']
            latitude_start = form.cleaned_data['latitude_start']
            longitude_end = form.cleaned_data['longitude_end']
            latitude_end = form.cleaned_data['latitude_end']

            route = RouteApiRequest(longitude_start,latitude_start,longitude_end,latitude_end)

            route_model = Route(longitude_start=longitude_start,latitude_start=latitude_start,longitude_end=longitude_end,latitude_end=latitude_end,distance=route.give_distance(),coordinates_json=route.give_coordinates())
            route_model.save()

            return redirect("/api/button")
    else:
        form = CoordinatesForm()
        return render(request, "button.html",{"form":form})