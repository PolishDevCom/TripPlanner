from rest_framework import viewsets
from api.serializers import RouteSerializer
from api.models import Route


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
