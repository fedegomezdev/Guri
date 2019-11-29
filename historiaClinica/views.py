from django.shortcuts import render,redirect, get_object_or_404
from .models import Paciente, Medico, Categoria
from .forms import PacienteForm, MedicoForm , CategoriaForm
from django.db.models import Q

# Create your views here.

def index(request):
    pacientes = Paciente.objects.filter(estado=True)
    medicos = Medico.objects.filter(estado = True)
    return render(request, 'historiaClinica/index.html', {'pacientes': pacientes, 'medicos': medicos})

def pacientes(request):
    queryset = request.GET.get('buscar')
    pacientes = Paciente.objects.filter( estado = True )[:20]
    if queryset:
        pacientes = Paciente.objects.filter(Q(numeroDoc__icontains = queryset) | Q(nombre__icontains = queryset) | Q(apellido__icontains = queryset)).distinct()
    return render(request, 'historiaClinica/pacientes.html', {'pacientes': pacientes}) 


def crearPaciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('pacientes')

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



######           MEDICOS             #####

def medicos(request):
    queryset = request.GET.get('buscar')
    medicos = Medico.objects.filter( estado = True )
    if queryset:
        medicos = Medico.objects.filter(Q(numeroDoc__icontains = queryset) | Q(nombre__icontains = queryset) | Q(apellido__icontains = queryset)).distinct()
    return render(request, 'historiaClinica/medicos.html', {'medicos': medicos}) 


def crearMedico(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('medicos')

    else:
        form = MedicoForm()
    return render(request , 'historiaClinica/crear-medico.html' , {'form': form})    



def eliminarMedico(request, id):
    medico = Medico.objects.get(id = id)        
    medico.eliminar()
    
    return redirect('medicos')    


def modificarMedico(request, id):
    medico = get_object_or_404(Medico, id = id, estado = True)
    form = MedicoForm(instance = medico)
    if request.method == 'POST':
        form = MedicoForm(request.POST, instance = medico)
        if form.is_valid():
            form.save()
            return redirect('medicos')
    return render(request, 'historiaClinica/crear-medico.html',{'form': form})     




#####      Categorias   ######
def categorias(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
    #    nombre = request.POST.get("cat")
    #   nuevo = Categoria.objects.create(nombre = nombre)
    #    nuevo.save()
            return redirect('categorias')
    form = CategoriaForm()
    return render(request, 'historiaClinica/categorias.html', { 'categorias': categorias, 'form':form})


def medicosCategorias(request, id ):
    
    medicos = Medico.objects.filter(categoria = id)
    categoria = Categoria.objects.get(id = id)
    return render(request, 'historiaClinica/medicos.html', {'medicos': medicos , 'categoria': categoria})    