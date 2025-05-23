from .models import Kunde, Schienenabschnitt
from rest_framework import serializers


class SchienenabschnittSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schienenabschnitt
        fields = '__all__'
        read_only_fields = ['updated_at']



class KundeSerializer(serializers.ModelSerializer):
    schienenabschnitte = SchienenabschnittSerializer(many=True, read_only=True)

    class Meta:
        model = Kunde
        fields = ['id', 'name', 'email', 'telefon', 'adresse', 'schienenabschnitte', 'updated_at']
        read_only_fields = ['updated_at']
