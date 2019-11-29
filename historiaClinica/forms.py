from django import forms
from .views import Paciente,Medico, Categoria

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'tipoDocumento', 'numeroDoc','telefono', 'celular', 'fechaNacimiento', 'correo', 'obraSocial']
        labels = {
            'nombre': 'Nombre',
            'apellido' : 'Apellido',
            'tipoDocumento': 'Tipo Documento',
            'numeroDoc': 'Número Documento',
            'telefono': 'Teléfono',
            'celular': 'Celular',
            'fechaNacimiento': 'Fecha de Nacimiento',
            'correo': 'Correo electrónico',
            'obraSocial':'Obra Social'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del paciente',
                    'id': 'nombre'
                }
            ),
            'apellido': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el apellido del paciente',
                    'id': 'apellido'
                }
            ),
            'tipoDocumento': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Tipo de Documento',
                    'id': 'tipoDocumento'
                }
            ),
            'numeroDoc': forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Número Documento',
                    'id': 'numeroDoc',
                    'min': '8888888',
                    'max':'100000000'
                }
            ),
            'telefono': forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Telefono',
                    'id': 'telefono'
                }
            ),
            'celular': forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Celular',
                    'id': 'celular'
                }
            ),
            'fechaNacimiento': forms.DateInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'DD/MM/AAAA',
                    'id': 'fechaNacimiento'
                }
            ),
            'correo': forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Correo@correo.com',
                    'id': 'correo'
                }
            ),
            'obraSocial': forms.Select(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Obra Social',
                    'id': 'obraSocial'
                }
            )
        }




class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nombre', 'apellido', 'tipoDocumento', 'numeroDoc','telefono', 'celular', 'fechaNacimiento', 'correo', 'horaIng', 'horaSalida', 'turnoMax','categoria']
        labels = {
            'nombre': 'Nombre',
            'apellido' : 'Apellido',
            'tipoDocumento': 'Tipo Documento',
            'numeroDoc': 'Número Documento',
            'telefono': 'Teléfono',
            'celular': 'Celular',
            'fechaNacimiento': 'Fecha de Nacimiento',
            'correo': 'Correo electrónico',
            'categoria':'Categoría',
            'horaIng': 'Hora de Ingreso',
            'horaSalida': 'Hora de Salida',
            'turnoMax': 'Turnos máximos'

        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del médico',
                    'id': 'nombre'
                }
            ),
            'apellido': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el apellido del médico',
                    'id': 'apellido'
                }
            ),
            'tipoDocumento': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Tipo de Documento',
                    'id': 'tipoDocumento'
                }
            ),
            'numeroDoc': forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Número Documento',
                    'id': 'numeroDoc',
                    'min': '8888888',
                    'max':'100000000'
                }
            ),
            'telefono': forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Teléfono',
                    'id': 'telefono'
                }
            ),
            'celular': forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Celular',
                    'id': 'celular'
                }
            ),
            'fechaNacimiento': forms.DateInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'DD/MM/AAAA',
                    'id': 'fechaNacimiento'
                }
            ),
            'correo': forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Correo@correo.com',
                    'id': 'correo'
                }
            ),
            'categoria': forms.Select(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Categoría',
                    'id': 'categoria'
                }
            ),
            'horaIng': forms.DateInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Hora de Ingreso',
                    'id': 'horaIng'
                }
            ),
            'horaSalida': forms.DateInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Hora de Salida',
                    'id': 'horaSalida'
                }
            ),
            'turnoMax': forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'',
                    'id': 'Turnos máximos'
                }
            )
        }



class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control col col-md-3 mr-2',
                    'placeholder':'Ingrese el nombre',
                    'id': 'nombre'
                }
            )
            }