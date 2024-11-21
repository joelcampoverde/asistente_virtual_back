from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status, viewsets
from .models import Evento
from .serializers import EventoSerializer
from django.contrib.auth.models import User

class EventoView(viewsets.ModelViewSet):
    serializer_class= EventoSerializer
    queryset= Evento.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retorna los eventos relacionados con la agenda del usuario autenticado
        return Evento.objects.filter(agenda__usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(agenda=self.request.user.agenda)
