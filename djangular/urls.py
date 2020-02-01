from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('layerfive.urls', namespace='api')),
    path('admin/', admin.site.urls),
]
