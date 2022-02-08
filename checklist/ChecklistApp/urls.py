
from django.urls import path,  re_path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('/Actividades/<int:id_checklist>', views.Actdetalle, name='Actividades'),
    path('/Checklist/Crear_Checklist ', views.Crear_check, name='crearchecklist'),
    path('/Checklist/eliminar/<int:id_checklist>/',views.eliminar_checklist, name='eliminarchecklist'),
    path('/Checklist/modificar/<int:pk>/',views.ActualizarChecklist.as_view() , name = 'editarchecklist'),
    path('/Actividades/CrearActividad/<int:id_checklist>', views.Crear_actividad, name = 'crearactividad'),
    path('/Actividades/eliminar/<int:id_actividad>',views.eliminar_actividad, name='eliminaractividad'),
    path('/Actividades/modificar/<int:id_actividad>/', views.editar_actividad, name = 'editaractividad'),
    path('/Actividades/eliminarModal/<int:id_actividad>/', views.AbrirModalEliminarAct, name = 'abrirmodaleliminaract'),
    path('/Checklist/eliminarModal/<int:id_checklist>/', views.AbrirModalEliminarCheck, name = 'abrirmodaleliminarcheck'),
    path ('/Actividad/ModificarUnCheck/<int:id_actividad>/', views.UpdateUnCheck,name= 'actualizauncheck'),
    path ('/Actividad/ModificarCheck/<int:id_actividad>/', views.UpdateCheck,name= 'actualizacheck'),


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