from django.apps import AppConfig


class AsistenteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'asistente'

    def ready(self):
        # Importa las señales
        import asistente.signals
