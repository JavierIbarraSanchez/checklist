from dataclasses import field
from django import forms

from .widgets import DatePickerInput
from .models import *

class Checklistform(forms.ModelForm):

    class Meta: 
        model = Checklist
        fields = ['fecha_plazo','nombre_checklist','descripcion_checklist']

        widgets =  {
            'fecha_plazo':DatePickerInput(format=('%Y-%m-%d')),
        }


class Actividadform(forms.ModelForm):

    class Meta: 
        model = Actividad
        fields = ['nombre_actividad','descripcion_actividad','actividad_realizada','id_checklist']