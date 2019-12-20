from django.shortcuts import render,redirect, get_object_or_404
from .models import Paciente, Medico, Categoria, ObraSocial, Turno
from .forms import PacienteForm, MedicoForm , CategoriaForm, ObraSocialForm, TurnoForm
from django.db.models import Q

# Create your views here.

def index(request):
    pacientes = Paciente.objects.filter(estado=True)
    medicos = Medico.objects.filter(estado = True)
    turnos = Turno.objects.filter(estado = False)
    return render(request, 'historiaClinica/index.html', {'pacientes': pacientes, 'medicos': medicos, 'turnos': turnos})

def pacientes(request):
    queryset = request.GET.get('buscar')
    pacientes = Paciente.objects.filter( estado = True )
    if queryset:
        pacientes = Paciente.objects.filter(Q(numeroDoc__icontains = queryset) | Q(nombre__icontains = queryset) | Q(apellido__icontains = queryset)).distinct()
    return render(request, 'historiaClinica/pacientes.html', {'pacientes': pacientes}) 


def unPaciente(request,id):
    paciente = Paciente.objects.get(id = id)
    turnos = Turno.objects.filter(paciente = id)
    if turnos.count() < 1:
        turnos = None
        return render(request, 'historiaClinica/unpaciente.html', {'paciente': paciente, 'turnos':turnos})
    return render(request, 'historiaClinica/unpaciente.html', {'paciente': paciente, 'turnos':turnos})
      


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


def unMedico(request,id):
    medico = Medico.objects.get(id = id)
    turnos = Turno.objects.filter(medico = id)
    if turnos.count() < 1:
        turnos = None
        return render(request, 'historiaClinica/unmedico.html', {'medico': medico, 'turnos':turnos})
    return render(request, 'historiaClinica/unmedico.html', {'medico': medico, 'turnos':turnos})

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
    #categoria = Categoria.objects.get(id = id)
    return render(request, 'historiaClinica/medicos.html', {'medicos': medicos })    



##### OBRAS SOCIALES #####
def obraSocial(request):
    obrassociales = ObraSocial.objects.all()
    if request.method == 'POST':
        form = ObraSocialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('obrasocial')
    form = ObraSocialForm()
    return render(request, 'historiaClinica/obrasocial.html', { 'obrassociales': obrassociales, 'form':form})


def pacientesObra(request, id ): 
    pacientes = Paciente.objects.filter(obraSocial = id)
    #obrasocial = ObraSocial.objects.get(id = id)
    return render(request, 'historiaClinica/pacientes.html', {'pacientes': pacientes })



#### TURNOS ####

def turnos(request):
    turnos = Turno.objects.all()
    return render(request, 'historiaClinica/turnos.html', {'turnos': turnos})   


def crearTurno(request):
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('turnos')
    else:
        form = TurnoForm()
    return render(request , 'historiaClinica/crear-turno.html' , {'form': form})  



def turnoPrueba(request):
    if request.method == 'POST':   
        dniPaciente= request.POST['dniP']
        dniMedico = request.POST['dniM']
        fecha = request.POST['fecha']
        hora= request.POST['hora']
        descripcion = request.POST['descripcion']        
        paciente = Paciente.objects.get(numeroDoc = dniPaciente)
        medico = Medico.objects.get(numeroDoc = dniMedico)
        try:
            Turno.objects.get_or_create(paciente= Paciente(id=paciente.id), medico= Medico(id=medico.id), hora = hora , horario = fecha, descripcion = descripcion)
            return redirect('turnos')
        except:
            error = 'Complete los campos de forma correcta'
            return render(request, 'historiaClinica/turnoprueba.html', {'error': error})    
        """  turno.paciente = paciente.id
        turno.medico = medico.id
        turno.hora = hora
        turno.fecha = fecha
        turno.save() """
        
    return render(request, 'historiaClinica/turnoprueba.html')       

        
         