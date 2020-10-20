from rest_framework import viewsets
from APIsApp.serializers import RouteSerializer
from APIsApp.models import Route


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer