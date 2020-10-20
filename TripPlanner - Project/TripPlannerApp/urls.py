from django.urls import path, include
from rest_framework.routers import DefaultRouter
from TripPlannerApp import views


router = DefaultRouter()
router.register('trips', views.TripViewSet, basename="trips")
router.register(r'registeruser', views.RegisterUserView, basename="register_user")

app_name = 'TripPlannerApp'

urlpatterns = [
    path('', include(router.urls)),
]
