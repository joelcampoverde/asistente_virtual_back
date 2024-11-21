from django.contrib import admin
from .models import Agenda, Evento, TipoEvento, Modalidad
# Register your models here.

admin.site.register(Agenda)
admin.site.register(Evento)
admin.site.register(TipoEvento)
admin.site.register(Modalidad)
