# urls.py
# Routes HTTP requests to the appropriate view logic, including the API endpoints

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from verkaufstool import views

# Registering API endpoints for automatic URL routing using DRF's router
router = routers.DefaultRouter()
router.register(r'kunden', views.KundeViewSet)
router.register(r'schienenabschnitte', views.SchienenabschnittViewSet)

# Defining URL patterns for the project
urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin interface
    path('letzte-aenderung/', views.letzte_aenderung, name='letzte_aenderung'),  # Custom endpoint to get the latest update timestamp
    path('', include(router.urls)),  # Automatically includes registered API viewsets
]
