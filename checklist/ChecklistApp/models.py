
from asyncio.windows_events import NULL
from wsgiref.handlers import format_date_time
from django.db import models



class Checklist(models.Model):
    id_checklist= models.AutoField(primary_key=True)
    fecha_creacion = models.DateField(auto_now_add=True, blank=True)
    fecha_plazo = models.DateField()
    nombre_checklist = models.CharField(max_length=250)
    descripcion_checklist = models.TextField(max_length=250)
    
    
    class Meta:
        
        db_table = 'checklist'
    def __str__(self):
        return self.nombre_checklist
   

# Create your models here.
class Actividad(models.Model):
    id_actividad = models.AutoField(primary_key=True)
    nombre_actividad = models.CharField(max_length=250)
    descripcion_actividad = models.TextField(max_length=500)
    actividad_realizada = models.BooleanField(default=False)
    id_checklist = models.ForeignKey(Checklist ,on_delete=models.CASCADE, db_column='id_checklist')



    class Meta:
        db_table = 'actividad'
    
    def __str__(self):
        return self.nombre_actividad

