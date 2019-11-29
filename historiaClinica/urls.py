from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pacientes/', views.pacientes , name='pacientes'),
    path('pacientes/crear-paciente', views.crearPaciente , name='crear-paciente'),
    path('pacientes/eliminar-paciente/<int:id>', views.eliminarPaciente , name='eliminar-paciente'),
    path('pacientes/modificar-paciente/<int:id>', views.modificarPaciente , name='modificar-paciente'),
    path('medicos/', views.medicos , name='medicos'),
    path('medicos/crear-medico', views.crearMedico , name='crear-medico'),
    path('medicos/eliminar-medico/<int:id>', views.eliminarMedico , name='eliminar-medico'),
    path('medicos/modificar-medico/<int:id>', views.modificarMedico , name='modificar-medico'),
    path('categorias/', views.categorias , name='categorias'),
    path('categorias/medicos-categorias/<int:id>', views.medicosCategorias , name='medicos-categorias'),    
]
