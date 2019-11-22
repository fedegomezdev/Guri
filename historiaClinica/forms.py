from django import forms
from .views import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'tipoDocumento', 'numeroDoc','telefono', 'celular', 'fechaNacimiento', 'correo', 'obraSocial']
        labels = {
            'nombre': 'Nombre',
            'apellido' : 'Apellido',
            'tipoDocumento': 'Tipo Documento',
            'numeroDoc': 'Numero Documento',
            'telefono': 'Telefono',
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
            'numeroDoc': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Numero Documento',
                    'id': 'numeroDoc'
                }
            ),
            'telefono': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Telefono',
                    'id': 'telefono'
                }
            ),
            'celular': forms.TextInput(
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