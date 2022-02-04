from dataclasses import field
from django import forms
from .models import *

class Checklistform(forms.ModelForm):

    class Meta: 
        model = Checklist
        fields = ['fecha_plazo','nombre_checklist','descripcion_checklist','favorito']