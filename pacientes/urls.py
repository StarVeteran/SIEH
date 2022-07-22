from django.urls import path

from django.contrib.auth import views as auth_views

from . import views



urlpatterns = [

    path('', views.home, name="inicio"),
    path('registro/',views.registro,name='registro'),
    path('login/',views.loginPag,name='login'),
    path('logout/',views.logoutUsuario,name='logout'),

    path('ver_perfil/',views.verPerfil,name='ver_perfil'),
    path('editar_perfil/',views.editarPerfil,name='editar_perfil'),
    
    path('Pacientes', views.AllPacientes, name="AllPacientes"),
    path('TusEventos', views.TusEventos, name="TusEventos"),


    # ------------------- EVENTOS FORMATIVOS -------------
    path('ArchivoClinico/',views.ArchivoClinico, name="ArchivoClinico"),
    path('ver_DatosPaciente<str:pk>/', views.DatosPaciente, name="DatosPaciente"),
    path('editar_paciente/<str:pk>', views.updatePaciente, name="updatePaciente"),
    path('crear_paciente_hospitalizacion/<str:pk>/', views.createPacienteHospitalizacion, name="createPacienteHospitalizacion"),
    path('crear_paciente_urgencias/<str:pk>/', views.createPacienteUrgencias, name="createPacienteUrgencias"),
    path('borrar_propuesta/<str:pk>/', views.deletePropuesta, name="deletePropuesta"),
    path('DatosPacientes', views.AllDatosPacientes, name="AllDatosPacientes"),
    path('Export', views.export, name="export"),
    path('Buscar', views.BuscarPaciente, name="buscador"),
    path('DatosSIOH', views.Expaciente_list, name="Expaciente_list"),


]
