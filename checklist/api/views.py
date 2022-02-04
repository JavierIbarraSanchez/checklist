from django.shortcuts import render

from dataclasses import field
from email import message
from multiprocessing import context
from pyexpat import model
from django.shortcuts import get_object_or_404, redirect, render
from ChecklistApp.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import ActividadSerializer,ChecklistSerializer
from rest_framework import serializers
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def ActividadApiOverview(request):
    api_urls = {
        'all_actividades': '/',
        'Search by Nombre actividad': '/?nombre_actividad=actividad_name',
        'Add': '/create',
        'Update:': '/update/pk',
        'Delete': '/actividad/pk/delete'
    }
    return Response(api_urls)

@api_view(['GET'])
def ChecklistApiOverview(request):
    api_urls = {
        'all_checklist': '/',
        'Search by Nombre checklist': '/?nombre_checklist=checklist_name',
        'Add': '/create',
        'Update:': '/update/pk',
        'Delete': '/checklist/pk/delete'
    }
    return Response(api_urls)

@api_view(['POST'])
def crear_actividad(request):
    print(request.data)
    actividad = ActividadSerializer(data = request.data)

    if Actividad.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Ya existe esta actividad')
    print(actividad)
    if actividad.is_valid():
        actividad.save()
        return Response(actividad.data)
    else:
        return Response (status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def crear_checklist(request):
    #breakpoint()
    checklist = ChecklistSerializer(data = request.data)

    if Checklist.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Ya existe esta actividad')
        
    
    if checklist.is_valid():
        checklist.save()
        return Response(checklist.data)
    else:
        return Response (status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def ver_actividades(request):
    if request.query_params:
        actividad = Actividad.objects.filter(**request.query_param.dict())
    else:
        actividad = Actividad.objects.all()
    
    print(actividad.query)
    if actividad:
        data = ActividadSerializer(actividad,many=True)
        return Response(list(data.data))
    else: 
        return Response (status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def ver_checklist(request):
    if request.query_params:
        checklist = Checklist.objects.filter(**request.query_param.dict())
    else:
        checklist = Checklist.objects.all()
    
    if checklist:
        data = ChecklistSerializer(checklist,many = True)
        return Response(data.data)
    else: 
        return Response (status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_actividades(request,pk):
    actividad = Actividad.objects.get(pk=pk)
    data = ActividadSerializer(instance=actividad, data= request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response (status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_checklist(request,pk):
    checklist = Checklist.objects.get(pk=pk)
    data = ChecklistSerializer(instance=checklist, data= request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response (status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_actividad(request,pk):
    actividad = get_object_or_404(Actividad, pk=pk)
    actividad.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['DELETE'])
def delete_checklist(request,pk):
    checklist = get_object_or_404(Checklist, pk=pk)
    checklist.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
