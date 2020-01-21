from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pacientes/', views.pacientes , name='pacientes'),
    path('pacientes/<int:id>', views.unPaciente , name='un-paciente'),
    path('pacientes/crear-paciente', views.crearPaciente , name='crear-paciente'),
    path('pacientes/eliminar-paciente/<int:id>', views.eliminarPaciente , name='eliminar-paciente'),
    path('pacientes/modificar-paciente/<int:id>', views.modificarPaciente , name='modificar-paciente'),
    path('medicos/', views.medicos , name='medicos'),
    path('medicos/<int:id>', views.unMedico , name='un-medico'),
    path('medicos/crear-medico', views.crearMedico , name='crear-medico'),
    path('medicos/eliminar-medico/<int:id>', views.eliminarMedico , name='eliminar-medico'),
    path('medicos/modificar-medico/<int:id>', views.modificarMedico , name='modificar-medico'),
    path('categorias/', views.categorias , name='categorias'),
    path('categorias/medicos-categorias/<int:id>', views.medicosCategorias , name='medicos-categorias'),
    path('obrasocial/', views.obraSocial , name='obrasocial'),
    path('obrasocial/pacientes-obrasocial/<int:id>', views.pacientesObra , name='pacientes-obrasocial'),
    path('turnos/', views.turnos, name='turnos'),
    path('turnos/crear-turno', views.crearTurno, name='crear-turno'),
    path('turnos/eliminar-turno/<int:id>', views.eliminarTurno , name='eliminar-turno'),
    path('turnos/crear-turno/<int:id>', views.turnoPorPaciente , name='turnoPorPaciente'),
    path('turnos/crear-turno-medico/<int:id>', views.turnoPorMedico , name='turnoPorMedico'),
    path('turnos/modificar-turno/<int:id>', views.modificarTurno , name='modificar-turno')
]
