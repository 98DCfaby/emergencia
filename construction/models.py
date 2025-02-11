from django.db import models

from django.db import models
class Obra(models.Model):
    ESTADO_OPCIONES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
        ('Finalizado', 'Finalizado'),
    ]

    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    imagen = models.ImageField(upload_to='obras/', blank=True, null=True)
    estado = models.CharField(max_length=50, choices=ESTADO_OPCIONES, default='Activo')

    def __str__(self):
        return self.nombre
class PlanEmergencia(models.Model):
    ESTADO_OPCIONES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
        ('Finalizado', 'Finalizado'),
    ]
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='plan_imagenes/', null=True, blank=True)  # Campo de imagen
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now=True)
    estado = models.CharField(max_length=50, choices=ESTADO_OPCIONES, default='Activo')
    
    
    def __str__(self):
        return f"Plan de emergencia - {self.obra.nombre}"

class Contratista(models.Model):
    nombre = models.CharField(max_length=200)
    rut = models.PositiveBigIntegerField() 
    telefono = models.PositiveBigIntegerField()  
    email = models.EmailField()
    especialidad = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='contratistas/', null=True, blank=True)  # Campo de imagen

    
    def __str__(self):
        return self.nombre

class EquipoSeguridad(models.Model):
    TIPOS_EQUIPO = [
        ('Prevención', 'Prevención y Detección'),
        ('EPP', 'Equipo de Protección Personal'),
        ('Respuesta', 'Respuesta y Mitigación'),
        ('Comunicación', 'Comunicación de Emergencia'),
        ('Evacuación', 'Evacuación y Rescate'),
    ]
    ESTADO_OPCIONES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
        ('Finalizado', 'Finalizado'),
    ]
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50, choices=TIPOS_EQUIPO)
    cantidad = models.IntegerField()
    fecha_adquisicion = models.DateField()
    estado = models.CharField(max_length=50, choices=ESTADO_OPCIONES, default='Activo')
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='equipo_imagenes/', null=True, blank=True)  # Campo de imagen

    
    def __str__(self):
        return self.nombre