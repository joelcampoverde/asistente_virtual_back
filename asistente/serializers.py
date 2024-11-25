from rest_framework import serializers
from .models import Evento

class EventoSerializer(serializers.ModelSerializer):
    # Campo adicional para mostrar la descripción de la modalidad
    modalidad_descripcion = serializers.CharField(source='modalidad.descripcion', read_only=True)

    class Meta:
        model = Evento
        # fields = "__all__"
        exclude = ["agenda"]

    def create(self, validated_data):
        fecha_fin = validated_data.get('fecha_fin')
        if not fecha_fin:
            # Si fecha_fin es None o una cadena vacía, asignamos fecha_inicio
            validated_data['fecha_fin'] = validated_data['fecha_inicio']
        return super().create(validated_data)

    def update(self, instance, validated_data):
        fecha_fin = validated_data.get('fecha_fin')
        if not fecha_fin:
            validated_data['fecha_fin'] = validated_data.get('fecha_inicio', instance.fecha_inicio)
        return super().update(instance, validated_data)
