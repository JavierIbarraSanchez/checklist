from dataclasses import field
from email import message
from multiprocessing import context
from pyexpat import model
from tkinter.tix import CheckList
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
    
    checklist = Checklist.objects.all().order_by('id_checklist')

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
    actividad = Actividad.objects.filter(id_checklist = id_checklist).order_by('id_actividad')
    checklist = Checklist.objects.filter(id_checklist = id_checklist).order_by('id_checklist')

    id_string = str(id_checklist)
    #print(actividad)
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
    check = get_object_or_404(Checklist,id_checklist=id_checklist)
    id_foranea = check.id_checklist
    id_string = str(id_checklist)
    initial_data={
        'nombre_actividad': " ",
        'descripcion_actividad': " ",
        'actividad_realizada': "" ,
        'id_checklist': id_foranea,
    }
    if request.method == "POST":
        form = Actividadform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/%2FActividades/'+id_string)
    else:
        form = Actividadform(initial=initial_data)
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
    id_string = str(id_foranea)
    
    if request.method == "POST":
        form = Actividadform(request.POST,instance = check )
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/%2FActividades/'+id_string)
    else:
        form = Actividadform(instance= check )
    context = { 'form': form, 'id_actividad':id_actividad }
    return render(request,"actividad/Actedit.html",context)
    

def AbrirModalEliminarAct(request,**kwargs):
    id_actividad = kwargs.get('id_actividad')
    check =  get_object_or_404(Actividad,id_actividad=id_actividad)
    id_foranea = check.id_checklist.id_checklist
    id_string = str(id_foranea)

    context = {'id_actividad':id_actividad}
    return render(request,"actividad/EliminarAct.html",context)

class ActualizarActividad(UpdateView):
    model = Actividad
    form_class = Actividadform
    template_name = 'actividad/Actedit.html'
    success_url = reverse_lazy('Actividades')

    def get_context_data(self,**kgargs):
        context = super().get_context_data(**kgargs)
        context['Actividad'] = Checklist.objects.all()
        return context

def AbrirModalEliminarCheck(request,**kwargs):
    id_checklist = kwargs.get('id_checklist')
    check =  get_object_or_404(Checklist,id_checklist=id_checklist)

    context = {'id_checklist':id_checklist}
    return render(request,"checklist/EliminarChecklist.html",context)


def UpdateUnCheck(request,**kwargs):
    id_actividad = kwargs.get('id_actividad')
    check = get_object_or_404(Actividad,id_actividad= id_actividad)
    nombre_actividad =  check.nombre_actividad
    descripcion = check.descripcion_actividad
    id_foranea = check.id_checklist
    id_string = str(id_foranea)

    print(check)
    initial_data={
        'nombre_actividad':  nombre_actividad,
        'descripcion_actividad': descripcion,
        'actividad_realizada': False,
        'id_checklist': id_foranea,
    }
    print(initial_data)
    if request.method == "POST":
        form = Actividadform(request.POST,instance = check )
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/%2FActividades/'+id_string)
    else:
        form = Actividadform(initial=initial_data )
    context = { 'form': form, 'id_actividad':id_actividad }
    return render(request,"actividad/uncheck.html",context)


def UpdateCheck(request,**kwargs):
    id_actividad = kwargs.get('id_actividad')
    check = get_object_or_404(Actividad,id_actividad= id_actividad)
    nombre_actividad =  check.nombre_actividad
    descripcion = check.descripcion_actividad
    id_foranea = check.id_checklist
    id_string = str(id_foranea)

    print(check)
    initial_data={
        'nombre_actividad':  nombre_actividad,
        'descripcion_actividad': descripcion,
        'actividad_realizada': True,
        'id_checklist': id_foranea,
    }
    print(initial_data)
    if request.method == "POST":
        form = Actividadform(request.POST,instance = check )
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/%2FActividades/'+id_string)
    else:
        form = Actividadform(initial=initial_data )
    context = { 'form': form, 'id_actividad':id_actividad }
    return render(request,"actividad/check.html",context)
   

