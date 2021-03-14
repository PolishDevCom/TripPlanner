from rest_framework import viewsets

from django.contrib.auth.models import User

from planner.serializers import TripSerializer, UserSerializer
from planner.models import Trip



class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class RegisterUserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    