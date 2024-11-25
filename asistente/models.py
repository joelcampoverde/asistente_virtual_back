from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# class Usuario(models.Model):
#     id = models.AutoField(primary_key=True)
#     nombre = models.CharField(max_length=100)
#     correo_electronico = models.EmailField()
#     celular = models.CharField(max_length=20)
#     rol = models.CharField(max_length=50)
#     fecha_ingreso = models.DateTimeField()
#
#     def __str__(self):
#         return self.nombre
#

# class Docente(models.Model):
#     usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name="docente")
#     facultad = models.CharField(max_length=100)
#     cargo = models.CharField(max_length=100)
#     titulo = models.CharField(max_length=100)
#     zona_horaria = models.CharField(max_length=50)
#
#     def __str__(self):
#         return f"{self.usuario.nombre} - {self.cargo}"
#

# class ComandoVoz(models.Model):
#     id = models.AutoField(primary_key=True)
#     descripcion = models.CharField(max_length=200)
#     fecha_uso = models.DateTimeField()
#     usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="comandos_voz")
#
#     def __str__(self):
#         return self.descripcion
#

class Agenda(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="agenda")

    def __str__(self):
        return f"Agenda de {self.usuario.username}"


class TipoEvento(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion

class Modalidad(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE, related_name="eventos")
    tipo_evento = models.ForeignKey(TipoEvento, on_delete=models.CASCADE, related_name="eventos")
    modalidad = models.ForeignKey(Modalidad, on_delete=models.CASCADE, related_name="eventos")
    descripcion = models.CharField(max_length=200)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.descripcion
