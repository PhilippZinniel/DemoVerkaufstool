from django.contrib import admin

from .models import Kunde, Schienenabschnitt

# Register your models here.
admin.site.register(Kunde)
admin.site.register(Schienenabschnitt)