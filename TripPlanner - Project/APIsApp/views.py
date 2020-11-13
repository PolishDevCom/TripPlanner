from django.shortcuts import render, redirect
from rest_framework import viewsets
from APIsApp.serializers import RouteSerializer
from APIsApp.models import Route

from .routeapi import RouteApiRequest


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

def buttonSiteView(request):
    distance = ""
    coordinates = ""
    if request.method == "POST":
        route = RouteApiRequest(17.6865287,53.9324734,17.4627752,52.0239488)
        distance = route.give_distance()
        coordinates = route.give_coordinates()

    return render(request, "button.html",{"coordinates":coordinates,"distance":distance})