from django.contrib import admin
from .models import Agenda, Evento, TipoEvento, Modalidad
# Register your models here.

# Personalización para el modelo Agenda
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario')  # Campos que se mostrarán en la lista
    search_fields = ('usuario__username',)  # Permitir búsqueda por nombre de usuario
    list_filter = ('usuario',)  # Permite filtrar por usuario
    ordering = ('usuario',)  # Ordenar por nombre de usuario

# Personalización para el modelo TipoEvento
class TipoEventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')  # Mostrar id y descripción en la lista
    search_fields = ('descripcion',)  # Permite búsqueda por descripción

# Personalización para el modelo Modalidad
class ModalidadAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')  # Mostrar id y descripción en la lista
    search_fields = ('descripcion',)  # Permite búsqueda por descripción

# Personalización para el modelo Evento
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'agenda', 'tipo_evento', 'modalidad', 'descripcion', 'fecha_inicio', 'fecha_fin')  # Campos en la lista
    search_fields = ('descripcion',)  # Permite búsqueda por descripción
    list_filter = ('tipo_evento', 'modalidad', 'fecha_inicio')  # Filtros por tipo de evento, modalidad y fecha de inicio
    ordering = ('fecha_inicio',)  # Ordenar por fecha de inicio
    date_hierarchy = 'fecha_inicio'  # Permite filtrar eventos por fecha
admin.site.register(Agenda)
admin.site.register(Evento)
admin.site.register(TipoEvento)
admin.site.register(Modalidad)
