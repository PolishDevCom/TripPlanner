from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('planner/', include('planner.urls')),
    path('api/', include('api.urls')),
]
