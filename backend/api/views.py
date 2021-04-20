"""Stores ViewSets."""

from api.models import Places, Route
from api.serializers import PlacesSerializer, RouteSerializer
from rest_framework import viewsets


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class PlacesViewSet(viewsets.ModelViewSet):
    """ViewSet for class Places."""

    queryset = Places.objects.all()
    serializer_class = PlacesSerializer
