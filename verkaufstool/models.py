# models.py
# Defines the database schema for customers and track sections.

from django.db import models


class Kunde(models.Model):
    """Represents a customer who potentially owns track sections.

    Attributes:
        name (str): The unique name of the customer.
        email (str or None): Optional email address of the customer.
        telefon (str or None): Optional phone number.
        adresse (str or None): Optional postal address.
        updated_at (datetime): Timestamp of the last modification (auto-updated).
    """
    name = models.CharField(max_length=200, unique=True)
    email = models.EmailField(blank=True, null=True)
    telefon = models.CharField(max_length=20, blank=True, null=True)
    adresse = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns the string representation of the customer."""
        return self.name


class Schienenabschnitt(models.Model):
    """Represents a section of track belonging to a customer.

    Attributes:
        schienentyp (str or None): Optional type of rail (e.g. steel, aluminum).
        schienenhaerte (int or None): Optional hardness rating of the rail.
        maximale_geschwindigkeit (int or None): Optional max speed allowed on the track.
        laenge (float or None): Optional length of the track section in meters.
        kunde (Kunde): ForeignKey to the owning customer.
        updated_at (datetime): Timestamp of the last modification (auto-updated).
    """
    schienentyp = models.CharField(max_length=100, blank=False, null=False)
    schienenhaerte = models.PositiveIntegerField(blank=False, null=False)
    maximale_geschwindigkeit = models.PositiveIntegerField(blank=False, null=False)
    laenge = models.FloatField(blank=False, null=False)
    kunde = models.ForeignKey(Kunde, on_delete=models.CASCADE, related_name='schienenabschnitte')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns a string representation of the track section."""
        return f"{self.schienentyp} - L{self.laenge} - {self.kunde.name}"
