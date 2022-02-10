
from django.urls import path,  re_path
from api import views
urlpatterns = [
    #Apis urls
     path('', views.ApiOverview, name='apihome'),
    path('Actividad', views.ActividadApiOverview, name='actividad'),
    path('Checklist', views.ChecklistApiOverview, name='checklist'),
    path('Actividad/Crear/', views.crear_actividad, name='crear-actividad'),
    path('Checklist/Crear/', views.crear_checklist, name='crear-checklist'),
    path('Actividad/Ver/', views.ver_actividades, name='ver-actividades'),
    path('Checklist/Ver/', views.ver_checklist, name='ver-checklist'),
    path('Checklist/Modificar/<int:pk>/', views.update_checklist, name='modificar-checklist'),
    path('Actividad/Modificar/<int:pk>/', views.update_actividades, name='modificar-actividades'),
    path('Actividad/eliminar/<int:pk>', views.delete_actividad, name='eliminar-actividades'),
    path('Checklist/eliminar/<int:pk>', views.delete_checklist, name='eliminar-checklist'),

]