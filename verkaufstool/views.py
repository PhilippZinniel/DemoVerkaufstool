from django.db.models import Max
from django.http import HttpResponse, JsonResponse

from .models import Kunde, Schienenabschnitt
from rest_framework import permissions, viewsets

from verkaufstool.serializers import KundeSerializer, SchienenabschnittSerializer


# Create your views here.
def index(request):
    return HttpResponse("Hello, world! :)")

def letzte_aenderung(request):
    kunde_updated = Kunde.objects.aggregate(max_updated=Max('updated_at'))['max_updated']
    abschnitt_updated = Schienenabschnitt.objects.aggregate(max_updated=Max('updated_at'))['max_updated']

    letzte_aenderung = max(filter(None, [kunde_updated, abschnitt_updated]))  # entfernt None

    return JsonResponse({
        "letzte_aenderung": letzte_aenderung
    })

class KundeViewSet(viewsets.ModelViewSet):
    queryset = Kunde.objects.all()
    serializer_class = KundeSerializer
#    permission_classes = [permissions.IsAuthenticated]


class SchienenabschnittViewSet(viewsets.ModelViewSet):
    queryset = Schienenabschnitt.objects.all()
    serializer_class = SchienenabschnittSerializer
#    permission_classes = [permissions.IsAuthenticated]
