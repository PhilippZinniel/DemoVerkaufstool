# serializers.py
# Converts model instances to JSON and validates incoming data.

from .models import Kunde, Schienenabschnitt
from rest_framework import serializers


class SchienenabschnittSerializer(serializers.ModelSerializer):
    """Serializer for the Schienenabschnitt (track section) model.

    Serializes all fields of the Schienenabschnitt model.
    The 'updated_at' field is marked as read-only to prevent changes via the API.
    """

    class Meta:
        model = Schienenabschnitt
        fields = '__all__'
        read_only_fields = ['updated_at']


class KundeSerializer(serializers.ModelSerializer):
    """Serializer for the Kunde (customer) model.

    Includes a nested, read-only representation of related Schienenabschnitt instances.
    The 'updated_at' field is marked as read-only to prevent changes via the API.

    Attributes:
        schienenabschnitte (SchienenabschnittSerializer): A list of related
            Schienenabschnitt objects (read-only, many=True).
    """
    schienenabschnitte = SchienenabschnittSerializer(many=True, read_only=True)

    class Meta:
        model = Kunde
        fields = ['id', 'name', 'email', 'telefon', 'adresse', 'schienenabschnitte', 'updated_at']
        read_only_fields = ['updated_at']
