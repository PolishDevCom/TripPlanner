from django.urls import path, include
from rest_framework.routers import DefaultRouter
from APIsApp import views


router = DefaultRouter()
router.register(r'routes', views.RoutesViewSet, basename="routes")


app_name = 'APIsApp'

urlpatterns = [
    path('', include(router.urls)),
]
