from django.db import models


class Kunde(models.Model):
    name = models.CharField(max_length=200, unique=True)
    email = models.EmailField(blank=True, null=True)
    telefon = models.CharField(max_length=20, blank=True, null=True)
    adresse = models.TextField(blank=True, null=True)


class Schienenabschnitt(models.Model):
    schienentyp = models.CharField(max_length=100, blank=True, null=True)
    schienenhaerte = models.PositiveIntegerField(blank=True, null=True)
    maximale_geschwindigkeit = models.PositiveIntegerField(blank=True, null=True)
    laenge = models.FloatField(blank=True, null=True)
    kunde = models.ForeignKey(Kunde, on_delete=models.CASCADE, related_name='schienenabschnitte')
