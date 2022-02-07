from dataclasses import field
from django import forms
from .models import *

class Checklistform(forms.ModelForm):

    class Meta: 
        model = Checklist
        fields = ['id_checklist','fecha_plazo','nombre_checklist','descripcion_checklist']


class Actividadform(forms.ModelForm):

    class Meta: 
        model = Actividad
        fields = ['nombre_actividad','descripcion_actividad','actividad_realizada','id_checklist']