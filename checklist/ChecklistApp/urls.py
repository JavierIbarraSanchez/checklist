
from django.urls import path,  re_path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('/Actividades/', views.Actdetalle, name='Actividades'),
    path('/Checklist/Crear_Checklist ', views.Crear_check, name='crearchecklist'),
    path('/Checklist/eliminar/<int:id_checklist>/',views.eliminar_checklist, name='eliminarchecklist'),
    path('/Checklist/modificar/<int:id_checklist>/', views.editar_checklist, name = 'editarchecklist'),


    #Apis urls
    #path('api/Actividad', views.ActividadApiOverview, name='actividad'),
    #path('api/Checklist', views.ChecklistApiOverview, name='checklist'),
    #path('api/Actividad/Crear/', views.crear_actividad, name='crear-actividad'),
    #path('api/Checklist/Crear/', views.crear_checklist, name='crear-checklist'),
    #path('api/Actividad/Ver/', views.ver_actividades, name='ver-actividades'),
    #path('api/Checklist/Ver/', views.ver_checklist, name='ver-checklist'),
    #path('api/Checklist/Modificar/<int:pk>/', views.update_checklist, name='modificar-checklist'),
    #path('api/Actividad/Modificar/<int:pk>/', views.update_actividades, name='modificar-actividades'),
    #path('api/Actividad/eliminar/<int:pk>', views.delete_actividad, name='eliminar-actividades'),
    #path('api/Checklist/eliminar/<int:pk>', views.delete_checklist, name='eliminar-checklist'),

]