from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializers import RouteSerializer
from .models import Route
from .forms import CoordinatesForm
from .routeapi import RouteApiRequest


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
