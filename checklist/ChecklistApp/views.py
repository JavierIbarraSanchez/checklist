from dataclasses import field
from email import message
from multiprocessing import context
from pyexpat import model
from xml.etree.ElementTree import tostring
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from ChecklistApp.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from .serializers import ActividadSerializer,ChecklistSerializer
from rest_framework import serializers
from rest_framework import status
from .forms import *
from django.views.generic.edit import UpdateView
# Create your views here.

def index(request):
    
    checklist = Checklist.objects.all()

    #Formulario de posteo:
    
    if request.method == "POST":
        form = Checklistform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Checklistform()
    

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context = {'datos_check' : checklist,'form':form}
    )

def Actdetalle(request,**kwargs):
    id_checklist = kwargs.get('id_checklist')
    actividad = Actividad.objects.filter(id_checklist = id_checklist)
    checklist = Checklist.objects.filter(id_checklist = id_checklist)

    id_string = str(id_checklist)

    if request.method == "POST":
        form = Actividadform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/%2FActividades/'+id_string)
    else:
        form = Actividadform()
   

    
    return render(
        request,
        'actividad/Actdetalle.html',
         context = {'datos_act' : actividad, 'datos_check':checklist, 'form':form }
    )

def Crear_check(request):
    if request.method == "POST":
        form = Checklistform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Checklistform()
    context = { 'form':form}
    return render(request,'checklist/index.html',context)


def eliminar_checklist(request,**kwargs):
    id_checklist = kwargs.get('id_checklist')
    check =  get_object_or_404(Checklist,id_checklist=id_checklist)
    check.delete()
    return(redirect("home"))

class ActualizarChecklist(UpdateView):
    model = Checklist
    form_class = Checklistform
    template_name = 'checklist/Checkedit.html'
    success_url = reverse_lazy('home')

    def get_context_data(self,**kgargs):
        context = super().get_context_data(**kgargs)
        context['Checklist'] = Checklist.objects.all()
        return context

def editar_checklist(request,**kwargs):
    id_checklist = kwargs.get('id_checklist')
    check = Checklist.objects.get(id_checklist = id_checklist)
    if request.method == "POST":
        form = Checklistform(request.POST,instance = check )
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Checklistform(instance= check )
    context = { 'form': form }
    return render(request,"checklist/Checkedit.html",context)

def Crear_actividad(request,**kwargs):

    id_checklist = kwargs.get('id_checklist')
    check = Checklist.objects.get(id_checklist = id_checklist)
    id_string = str(id_checklist)

    if request.method == "POST":
        form = Actividadform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/%2FActividades/'+id_string)
    else:
        form = Actividadform()
    context = { 'form':form, 'check_id':check}
    return render(request,'actividad/ActCrear.html',context)

def eliminar_actividad(request,**kwargs):
    id_actividad = kwargs.get('id_actividad')
    check =  get_object_or_404(Actividad,id_actividad=id_actividad)
    id_foranea = check.id_checklist.id_checklist
    print(id_foranea)
    id_string = str(id_foranea)
    
    check.delete()
    return(redirect('http://127.0.0.1:8000/%2FActividades/'+id_string))


def editar_actividad(request,**kwargs):
    id_actividad = kwargs.get('id_actividad')
    check = Actividad.objects.get(id_actividad = id_actividad)
    id_foranea = check.id_checklist.id_checklist
    print(id_foranea)
    id_string = str(id_foranea)
    if request.method == "POST":
        form = Actividadform(request.POST,instance = check )
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/%2FActividades/'+id_string)
    else:
        form = Actividadform(instance= check )
    context = { 'form': form }
    return render(request,"actividad/Actedit.html",context)