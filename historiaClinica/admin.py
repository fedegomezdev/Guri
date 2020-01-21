from django.contrib import admin
from .models import Medico, Paciente, Turno, Categoria, Historial, ObraSocial

# Register your models here.
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Turno)
admin.site.register(Categoria)
admin.site.register(Historial)
admin.site.register(ObraSocial)

admin.site.site_header = 'Administración de Salud'

