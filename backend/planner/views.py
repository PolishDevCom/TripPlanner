from django.contrib.auth.models import User
from planner.models import Trip
from planner.serializers import TripSerializer, UserSerializer
from rest_framework import viewsets


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class RegisterUserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
