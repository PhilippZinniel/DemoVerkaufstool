# views.py
# Handles API endpoints for managing user profiles.

from django.db.models import Max
from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import Kunde, Schienenabschnitt
from rest_framework import permissions, viewsets

from verkaufstool.serializers import KundeSerializer, SchienenabschnittSerializer


@api_view(['GET'])
def letzte_aenderung(request):
    """Retrieve the latest update timestamp from Kunde and Schienenabschnitt models.

    This endpoint collects the maximum 'updated_at' timestamps from both
    Kunde and Schienenabschnitt models to determine the most recent update.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing the latest update timestamp
        under the key 'letzte_aenderung'. If both models have no entries,
        the value will be null.
    """
    kunde_updated = Kunde.objects.aggregate(max_updated=Max('updated_at'))['max_updated']
    abschnitt_updated = Schienenabschnitt.objects.aggregate(max_updated=Max('updated_at'))['max_updated']

    timestamps = list(filter(None, [kunde_updated, abschnitt_updated]))
    letzte_aenderung = max(timestamps) if timestamps else None

    return JsonResponse({
        "letzte_aenderung": letzte_aenderung
    })


class KundeViewSet(viewsets.ModelViewSet):
    """API endpoint for viewing and editing Kunde (Customer) instances.

    Provides standard CRUD actions for Kunde model.

    Attributes:
        queryset (QuerySet): All Kunde objects.
        serializer_class (Serializer): Serializer for Kunde model.
        permission_classes (list): Permissions for accessing this viewset.
   """
    queryset = Kunde.objects.all()
    serializer_class = KundeSerializer
    # permission_classes = [permissions.IsAuthenticated]


class SchienenabschnittViewSet(viewsets.ModelViewSet):
    """API endpoint for viewing and editing Schienenabschnitt (Track Section) instances.

    Provides standard CRUD actions for Schienenabschnitt model.

    Attributes:
        queryset (QuerySet): All Schienenabschnitt objects.
        serializer_class (Serializer): Serializer for Schienenabschnitt model.
        permission_classes (list): Permissions for accessing this viewset.
    """
    queryset = Schienenabschnitt.objects.all()
    serializer_class = SchienenabschnittSerializer
    # permission_classes = [permissions.IsAuthenticated]
