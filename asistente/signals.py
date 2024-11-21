# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Agenda

@receiver(post_save, sender=User)
def crear_agenda_usuario(sender, instance, created, **kwargs):
    if created:
        Agenda.objects.create(usuario=instance)
