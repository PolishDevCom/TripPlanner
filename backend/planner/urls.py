from django.urls import include, path
from planner import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("trips", views.TripViewSet, basename="trips")
router.register(
    r"registeruser", views.RegisterUserView, basename="register_user"
)

app_name = "planner"

urlpatterns = [
    path("", include(router.urls)),
]
