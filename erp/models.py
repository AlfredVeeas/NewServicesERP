from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, nombre='Nombre Predeterminado', **extra_fields):
        if not email:
            raise ValueError('El campo de correo electrónico es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, nombre=nombre, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, nombre='Administrador', **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Los superusuarios deben tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Los superusuarios deben tener is_superuser=True.')

        return self.create_user(email, password, nombre=nombre, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=255, default='Nombre Predeterminado')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

#-------------------TABLA DE FICHA NAVIO -------------------------------------------------------------------------
class FichaNavio(models.Model):
    Nave = models.CharField(max_length=255)
    Viaje = models.CharField(max_length=255)
    Puerto = models.CharField(max_length=255)
    Carga = models.CharField(max_length=255)
    Procedencia = models.CharField(max_length=255)
    TipoServicio = models.CharField(max_length=255)
    Armador = models.CharField(max_length=255)
    Agencia = models.CharField(max_length=255)
    ProximoPuerto = models.CharField(max_length=255)
    Encalado = models.CharField(max_length=3, choices=[('Si', 'Si'), ('No', 'No')])
    ETA = models.DateField()
    horaRegistroETA = models.TimeField()
    Bombasumergible = models.CharField(max_length=3, choices=[('Si', 'Si'), ('No', 'No')])
    Cubierta = models.CharField(max_length=3, choices=[('Si', 'Si'), ('No', 'No')])
    ShapeBox = models.CharField(max_length=3, choices=[('Si', 'Si'), ('No', 'No')])
    PCR = models.CharField(max_length=3, choices=[('Si', 'Si'), ('No', 'No')])
    horaRegistroPCR = models.TimeField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    cantidadPersonas = models.IntegerField()
    puerto = models.IntegerField()

    def __str__(self):
        return self.Nave
    
#----------------------TABLA DE FICHA Vehiculos-----------------------------------------------------------------------------   
# 
class FichaVehiculo(models.Model):
    TIPO_VEHICULO_CHOICES = [
        ('', 'Seleccione un tipo de vehículo'),
        ('Auto', 'Auto'),
        ('Camioneta', 'Camioneta'),
        ('Furgon', 'Furgon'),
        ('Camion', 'Camion'),
    ]

    TIPO_COMBUSTIBLE_CHOICES = [
        ('', 'Seleccione un tipo de combustible'),
        ('Diesel', 'Diesel'),
        ('Bencinero', 'Bencinero'),
    ]

    marca = models.CharField(max_length=255)  # Cambiado a CharField para texto
    fecha_ingreso = models.DateField()
    modelo = models.CharField(max_length=255)
    patente = models.CharField(max_length=10)  # Ajusta la longitud según sea necesario
    chasis = models.CharField(max_length=255)
    tipo_vehiculo = models.CharField(max_length=50, choices=TIPO_VEHICULO_CHOICES)
    tipo_combustible = models.CharField(max_length=50, choices=TIPO_COMBUSTIBLE_CHOICES)

    def __str__(self):
        return f'{self.marca} - {self.modelo} - {self.patente}'


#----------------------TABLA DE FICHA Quimico-----------------------------------------------------------------------------    
class FichaQuimico(models.Model):
    TIPO_QUIMICO_CHOICES = [
        ('OCN 01', 'OCN 01'),
        ('OCN 08', 'OCN 08'),
        ('Acido Clorhídrico', 'Acido Clorhídrico'),
        ('Hipoclorito', 'Hipoclorito'),
        ('Hold Coat', 'Hold Coat'),
    ]

    CAPACIDAD_BIN_CHOICES = [
        ('Lleno', 'Lleno (1000 lts) aprox'),
        ('Medio', 'Medio (500 lts) aprox'),
    ]

    LUGAR_ALMACENAMIENTO_CHOICES = [
        ('Taller', 'Taller'),
        ('Container', 'Container'),
    ]

    tipo_quimico = models.CharField(max_length=50, choices=TIPO_QUIMICO_CHOICES, default='OCN 01')
    fecha_registro = models.DateField()
    capacidad_bines = models.CharField(max_length=255, default='Lleno (1000 lts) aprox')
    lugar_almacenamiento = models.CharField(max_length=255, default='Taller')

    def __str__(self):
        return f'{self.tipo_quimico} - {self.fecha_registro}'
    
    #----------------------TABLA DE FICHA HERRAMIENTAS-----------------------------------------------------------------------------    
class FichaHerramientas(models.Model):
    marca = models.CharField(max_length=255)
    fecha_ingreso = models.DateField()
    modelo = models.CharField(max_length=255)
    cantidad_herramientas = models.IntegerField()
    
    TIPO_HERRAMIENTA_CHOICES = [
        ('Manual', 'Manual'),
        ('Mecanico', 'Mecanico'),
        # Agrega otros tipos según sea necesario
    ]
    
    tipo_herramienta = models.CharField(max_length=50, choices=TIPO_HERRAMIENTA_CHOICES)

    def __str__(self):
        return f'{self.marca} - {self.modelo} - Cantidad: {self.cantidad_herramientas}'

