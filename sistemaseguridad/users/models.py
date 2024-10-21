from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class EstatusUsuario(models.Model):
    nombre = models.CharField(max_length = 30)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    usuario_creacion = models.CharField(max_length = 203, default='admin')
    fecha_modificacion = models.DateTimeField(auto_now = True)
    usuario_modificacion = models.CharField(max_length = 203, default='admin')
    
    def __str__(self) -> str:
        return str(self.id) + ' - ' + self.nombre
    
    def __unicode__(self) -> str:
        return super().__unicode__()
    
class Genero(models.Model):
    nombre = models.CharField(max_length = 30)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    usuario_creacion = models.CharField(max_length = 203, default='admin')
    fecha_modificacion = models.DateTimeField(auto_now = True)
    usuario_modificacion = models.CharField(max_length = 203, default='admin')

    def __str__(self) -> str:
        return str(self.id) + ' - ' + self.nombre
    
    def __unicode__(self) -> str:
        return super().__unicode__()


class Empresa(models.Model):
    nombre = models.CharField(max_length = 100)
    direccion = models.CharField(max_length = 100)
    nit = models.CharField(max_length = 30)
    password_cantidad_mayusculas = models.IntegerField(default = 0)
    password_cantidad_minusculas = models.IntegerField(default = 0)
    password_cantidad_caracteres_especiales = models.IntegerField(default = 0)
    password_cantidad_caducidad_dias = models.IntegerField(default = 0)
    password_cantidad_numeros = models.IntegerField(default = 0)
    password_tamano = models.IntegerField(default = 0)
    password_intentos_antes_de_bloquear = models.IntegerField(default = 0)
    password_cantidad_preguntar_validar = models.IntegerField(default = 0)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    usuario_creacion = models.CharField(max_length = 203, default='admin')
    fecha_modificacion = models.DateTimeField(auto_now = True)
    usuario_modificacion = models.CharField(max_length = 203, default='admin')

    
    def __str__(self) -> str:
        return str(self.id) + ' - ' + self.nombre 
    
    def __unicode__(self) -> str:
        return super().__unicode__()

class Sucursal(models.Model):
    nombre = models.CharField(max_length = 30)
    direccion = models.CharField(max_length = 30)
    empresa = models.ForeignKey(Empresa, on_delete = models.DO_NOTHING, blank = True, null = True)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    usuario_creacion = models.CharField(max_length = 203, default='admin')
    fecha_modificacion = models.DateTimeField(auto_now = True)
    usuario_modificacion = models.CharField(max_length = 203, default='admin')

    def __str__(self) -> str:
        return str(self.id) + ' - ' + self.nombre
    
    def __unicode__(self) -> str:
        return super().__unicode__()

class UsuarioManager(BaseUserManager):
    def crear_usuario(self, correo_electronico, password=None, **extra_fields):
        if not correo_electronico:
            raise ValueError('El correo electrónico debe ser proporcionado')
        email = self.normalize_email(correo_electronico)
        user = self.model(correo_electronico=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def crear_superusuario(self, correo_electronico, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(correo_electronico, password, **extra_fields)

class Usuario(models.Model):
    # id_usuario = models.AutoField(primary_key = True, blank=False, null=False)
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    fecha_nacimiento = models.DateField(blank = True, null = True)
    estatus_usuario = models.ForeignKey(EstatusUsuario, on_delete = models.DO_NOTHING, blank = True, null = True, default = 0)
    password = models.CharField(max_length = 30)
    genero = models.ForeignKey(Genero, on_delete = models.DO_NOTHING, blank = True, null = True, default = 0)
    ultima_fecha_ingreso = models.DateTimeField(blank=True, null=True)
    intentos_de_acceso = models.IntegerField(default = 0)
    # sesion_actual = models.CharField(max_length = 30, blank = True, null = True)
    ultima_fecha_cambio_password = models.DateTimeField(blank=True, null=True)
    correo_electronico = models.CharField(max_length = 100, blank = True, null = True)
    requiere_cambiar_password = models.BooleanField(default = False)
    fotografia = models.CharField(max_length = 300, blank = True, null = True)
    telefono_movil = models.CharField(max_length = 30, blank = True, null = True)
    sucursal = models.ForeignKey(Sucursal, on_delete = models.DO_NOTHING, blank = True, null = True)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    usuario_creacion = models.CharField(max_length = 203, default='admin')
    fecha_modificacion = models.DateTimeField(auto_now = True)
    usuario_modificacion = models.CharField(max_length = 203, default='admin')

    USERNAME_FIELD = 'correo_electronico'  # Indica que este será el campo usado para el login
    REQUIRED_FIELDS = ['nombre', 'apellido']  # Campos requeridos al crear un superusuario

    objects = UsuarioManager()  # Enlaza el manager
    
    def __str__(self) -> str:
        return f'{self.id} - {self.nombre} {self.apellido}'

    
class UsuarioPregunta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete = models.DO_NOTHING, blank = True, null = True)
    pregunta = models.CharField(max_length = 100)
    respuesta = models.CharField(max_length = 100)
    orden_pregunta = models.IntegerField(default = 1)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    usuario_creacion = models.CharField(max_length = 203, default='admin')
    fecha_modificacion = models.DateTimeField(auto_now = True)
    usuario_modificacion = models.CharField(max_length = 203, default='admin')
    
    def __str__(self) -> str:
        return str(self.id)  + ' - ' + self.pregunta 
    
class Rol(models.Model):
    nombre = models.CharField(max_length = 100)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    usuario_creacion = models.CharField(max_length = 203, default='admin')
    fecha_modificacion = models.DateTimeField(auto_now = True)
    usuario_modificacion = models.CharField(max_length = 203, default='admin')
    
    def __str__(self) -> str:
        return str(self.id) + ' - ' + self.nombre
    
class UsuarioRol(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete = models.DO_NOTHING, blank = True, null = True)
    rol = models.ForeignKey(Rol, on_delete = models.DO_NOTHING, blank = True, null = True)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    usuario_creacion = models.CharField(max_length = 203, default='admin')
    fecha_modificacion = models.DateTimeField(auto_now = True)
    usuario_modificacion = models.CharField(max_length = 203, default='admin')
    
    def __str__(self) -> str:
        return str(self.id)  + ' - ' + str(self.rol) + ' - ' + str(self.usuario) 

class Modulo(models.Model):
    nombre = models.CharField(max_length = 100)
    orden_menu = models.IntegerField(default = 1)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    usuario_creacion = models.CharField(max_length = 203, default='admin')
    fecha_modificacion = models.DateTimeField(auto_now = True)
    usuario_modificacion = models.CharField(max_length = 203, default='admin')
    
    def __str__(self) -> str:
        return str(self.id) + ' - ' + self.nombre
    
class Menu(models.Model):
    modulo = models.ForeignKey(Modulo, on_delete = models.DO_NOTHING, blank = True, null = True)
    nombre = models.CharField(max_length = 100)
    orden_menu = models.IntegerField(default = 1)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    usuario_creacion = models.CharField(max_length = 203, default='admin')
    fecha_modificacion = models.DateTimeField(auto_now = True)
    usuario_modificacion = models.CharField(max_length = 203, default='admin')
    
    def __str__(self) -> str:
        return str(self.id) + ' - ' + self.nombre

class Opcion(models.Model):
    menu = models.ForeignKey(Menu, on_delete = models.DO_NOTHING, blank = True, null = True)
    nombre = models.CharField(max_length = 100)
    orden_menu = models.IntegerField(default = 1)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    usuario_creacion = models.CharField(max_length = 203, default='admin')
    fecha_modificacion = models.DateTimeField(auto_now = True)
    usuario_modificacion = models.CharField(max_length = 203, default='admin')
    
    def __str__(self) -> str:
        return str(self.id) + ' - ' + self.nombre

class RolOpcion(models.Model):
    rol = models.ForeignKey(Rol, on_delete = models.DO_NOTHING, blank = True, null = True)
    opcion = models.ForeignKey(Opcion, on_delete = models.DO_NOTHING, blank = True, null = True)
    alta = models.BooleanField(default = True)
    bajo = models.BooleanField(default = True)
    cambio = models.BooleanField(default = True)
    imprimir = models.BooleanField(default = True)
    exportar = models.BooleanField(default = True)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    usuario_creacion = models.CharField(max_length = 203, default='admin')
    fecha_modificacion = models.DateTimeField(auto_now = True)
    usuario_modificacion = models.CharField(max_length = 203, default='admin')
    
    def __str__(self) -> str:
        return str(self.id) + ' - ' + str(self.rol) + ' - ' + str(self.opcion)
    
class TipoAcceso(models.Model): 
    nombre = models.CharField(max_length = 100) 
    fecha_creacion = models.DateTimeField(auto_now_add = True) 
    usuario_creacion = models.CharField(max_length = 203, default='admin') 
    fecha_modificacion = models.DateTimeField(auto_now = True) 
    usuario_modificacion = models.CharField(max_length = 203, default='admin') 
    
    def __str__(self) -> str: 
        return str(self.id) + ' - ' + self.nombre

class BitacoraAcceso(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete = models.DO_NOTHING, blank = True, null = True)
    tipo_acceso = models.ForeignKey(TipoAcceso, on_delete = models.DO_NOTHING, blank = True, null = True)
    fecha_acceso = models.DateTimeField(auto_now_add = True)
    http_user_agent = models.CharField(max_length = 100, blank = True, null = True)
    direccion_ip = models.CharField(max_length = 100, blank = True, null = True)
    accion = models.CharField(max_length = 100, blank = True, null = True)
    sistema_operativo = models.CharField(max_length = 100, blank = True, null = True)
    dispositivo = models.CharField(max_length = 100, blank = True, null = True)
    browser = models.CharField(max_length = 100, blank = True, null = True)
    sesion = models.CharField(max_length = 100, blank = True, null = True)

    def __str__(self) -> str:
        return str(self.id) + ' - ' + str(self.usuario) + ' - ' + str(self.tipo_acceso)
