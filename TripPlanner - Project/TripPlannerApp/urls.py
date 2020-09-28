from django.urls import path, include
from rest_framework.routers import DefaultRouter
from TripPlannerApp import views


router = DefaultRouter()
router.register('trips', views.TripViewSet, basename="trips")
router.register(r'users', views.UserViewSet, basename="users")

app_name = 'TripPlannerApp'

urlpatterns = [
    path('', include(router.urls)),
]
