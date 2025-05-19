from django.http import HttpResponse
from .models import Kunde, Schienenabschnitt
from rest_framework import permissions, viewsets

from verkaufstool.serializers import KundeSerializer, SchienenabschnittSerializer


# Create your views here.
def index(request):
    return HttpResponse("Hello, world! :)")


class KundeViewSet(viewsets.ModelViewSet):
    queryset = Kunde.objects.all()
    serializer_class = KundeSerializer
#    permission_classes = [permissions.IsAuthenticated]


class SchienenabschnittViewSet(viewsets.ModelViewSet):
    queryset = Schienenabschnitt.objects.all()
    serializer_class = SchienenabschnittSerializer
#    permission_classes = [permissions.IsAuthenticated]
