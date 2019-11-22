from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Categoria', max_length = 100, null = False, blank = False)
    fechaCreacion = models.DateField('Fecha creacion',default = timezone.now)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre

class ObraSocial(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 255)

    class Meta:
        verbose_name = "Obra Social"
        verbose_name_plural = "Obras Sociales"

    def __str__(self):
        return self.nombre    


class Medico(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre del Medico', max_length=55 , null = False, blank= False)
    apellido = models.CharField('Apellido del Medico', max_length=55 , null = False, blank= False)
    tipoDocumento = models.CharField(max_length= 20 ,null = True, blank= True)
    numeroDoc = models.CharField( max_length=8, null = False, blank= False)
    telefono = models.CharField('Telefono', max_length=20, null = True, blank = True)
    celular = models.CharField('Celular', max_length=20, null = True, blank = True)
    horaIng = models.DateField(null = True, blank = True)
    horaSalida = models.DateField(null = True, blank = True)
    turnoMax = models.IntegerField(null = True, blank = True)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE, null = True, blank= True)
    estado = models.BooleanField(default = True)
    fechaCreacion = models.DateField('Fecha creacion', default = timezone.now)
    fechaNacimiento = models.DateField('Fecha nacimiento', null = True)
    correo = models.EmailField('Email', blank = True, null = True )
    estado = models.BooleanField(default=True)
    fechaBaja = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Medico'
        verbose_name_plural = 'Medicos'

    def __str__(self):
        return '%s %s' %(self.nombre , self.apellido)

    def eliminar(self):
        self.fechaBaja = timezone.now()
        self.estado = False
        self.save()


class Paciente(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre del Paciente', max_length=55 , null = False, blank= False)
    apellido = models.CharField('Apellido del Paciente', max_length=55 , null = False, blank= False)
    tipoDocumento = models.CharField(max_length= 20 ,null = True, blank= True)
    numeroDoc = models.CharField(max_length=8)
    telefono = models.CharField(max_length=20, null = True, blank = True)
    celular = models.CharField(max_length=20, null = True, blank = True)
    fechaCreacion = models.DateField('Fecha creacion', default = timezone.now)
    fechaNacimiento = models.DateField('Fecha nacimiento', null = True)
    correo = models.EmailField('Email', blank = True, null = True )
    estado = models.BooleanField(default=True)
    obraSocial = models.ForeignKey(ObraSocial, on_delete=models.CASCADE , null = True , blank = True)
    fechaBaja = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return '%s %s' %(self.nombre , self.apellido)

    def eliminar(self):
        self.fechaBaja = timezone.now()
        self.estado = False
        self.save()


class Turno(models.Model):
    id = models.AutoField(primary_key = True)
    medico = models.ForeignKey(Medico, on_delete = models.CASCADE , null = True, blank = True)
    paciente = models.ForeignKey(Paciente, on_delete = models.CASCADE, null = True, blank = True)
    horario = models.DateField()
    fechaCreacion = models.DateField(default = timezone.now)

    class Meta:
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'


    def __str__(self):
        return self.paciente



class Historial(models.Model):
    id = models.AutoField(primary_key = True)
    paciente = models.ForeignKey(Paciente, on_delete = models.CASCADE)
    historial = RichTextField('Historia Clinica')
    fechaCreacion = models.DateField('Fecha de Creacion', auto_now = False, auto_now_add= True)
    fechaModificacion = models.DateField('Fecha de Modificacion', auto_now = True )

    class Meta:
        verbose_name = 'Historial'
        verbose_name_plural = 'Historiales'

    def __str__(self):
        return self.paciente



    