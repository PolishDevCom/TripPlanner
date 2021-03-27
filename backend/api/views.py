from api.models import Route
from api.serializers import RouteSerializer
from rest_framework import viewsets


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
