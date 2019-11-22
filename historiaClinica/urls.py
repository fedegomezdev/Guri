from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pacientes/', views.pacientes , name='pacientes'),
    path('pacientes/crear-paciente', views.crearPaciente , name='crear-paciente'),
    path('pacientes/eliminar-paciente/<int:id>', views.eliminarPaciente , name='eliminar-paciente'),
    path('pacientes/modificar-paciente/<int:id>', views.modificarPaciente , name='modificar-paciente'),
]
