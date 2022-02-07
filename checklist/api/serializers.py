
from rest_framework import serializers
from ChecklistApp.models import Actividad ,Checklist


class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = ['id_actividad','nombre_actividad','descripcion_actividad','actividad_realizada','id_checklist']

class ChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checklist
        fields = ('id_checklist','fecha_creacion','fecha_plazo','nombre_checklist','descripcion_checklist')
