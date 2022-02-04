"""checklist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib import admin
from django.urls import path,include
from ChecklistApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('ChecklistApp.urls')),
    path('api/',include('api.urls'))

    
   # path('Actividad/',ActividadListado.as_view(template_name = "actividad/listadoAct.html"), name ='leerActividad' ),
   # path('Checklist/',ChecklistListado.as_view(template_name = "checklist/listadoCheck.html"), name = 'LeerChecklist' ),
   # path('Actividad/Detalle/<int:pk>',ActividadDetalle.as_view(template_name = "actividad/Actdetalle.html"),name = 'ActDetalle'),
   # path('Checklist/Detalle/',ChecklistDetalle.as_view(template_name = "checklist/Checkdetalle.html"),name = 'CheckDetalle'),
   # path('Actividad/crear',ActividadCrear.as_view(template_name = "actividad/ActCrear.html"),name = 'ActCrear'),
   # path('Checklist/crear',ChecklistCrear.as_view(template_name = "actividad/CheckCrear.html"),name = 'CheckCrear'),
   # path('Actividad/editar/<int:pk>',ActividadActualizar.as_view(template_name = "actividad/Actedit.html"),name = 'ActEdit'),
   # path('Checklist/editar/<int:pk>',ChecklistActualizar.as_view(template_name = "checklist/Checkedit.html"),name = 'CheckEdit'),
   # path('Actividad/eliminar/<int:pk>',ActividadEliminar.as_view(),name = 'Actdelete'),
   # path('Checklist/eliminar/<int:pk>',ActividadEliminar.as_view(),name = 'Checkdelete')
]
