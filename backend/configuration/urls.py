"""Urls"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("planner/", include("planner.urls")),
    path("api/", include("api.urls")),
    path("authentication/", include("accounts.urls")),
]
