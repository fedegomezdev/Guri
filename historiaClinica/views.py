from django.shortcuts import render,redirect, get_object_or_404
from .models import Paciente
from .forms import PacienteForm

# Create your views here.

def index(request):
    return render(request, 'historiaClinica/index.html')

def pacientes(request):
    pacientes = Paciente.objects.filter( estado = True )
    return render(request, 'historiaClinica/pacientes.html', {'pacientes': pacientes}) 


def crearPaciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('index')
    else:
        form = PacienteForm()
    return render(request , 'historiaClinica/crear-paciente.html' , {'form': form})    


def eliminarPaciente(request, id):
    paciente = Paciente.objects.get(id = id)        
    paciente.eliminar()
    
    return redirect('pacientes')
   

def modificarPaciente(request, id):
    paciente = get_object_or_404(Paciente, id = id, estado = True)
    form = PacienteForm(instance = paciente)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance = paciente)
        if form.is_valid():
            form.save()
            return redirect('pacientes')
    return render(request, 'historiaClinica/crear-paciente.html',{'form': form})        