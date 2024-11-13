from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class EstatusUsuario(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_creacion = models.CharField(max_length=203, null=True, blank=True)  # Permitir valores nulos
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_modificacion = models.CharField(max_length=203, null=True, blank=True)  # Permitir valores nulos
    
    def __str__(self) -> str:
        return str(self.id) + ' - ' + self.nombre
    
class Genero(models.Model):
    nombre = models.CharField(max_length = 30)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    usuario_creacion = models.CharField(max_length = 203, default='admin')
    fecha_modificacion = models.DateTimeField(null=True, blank=True)
    usuario_modificacion = models.CharField(max_length = 203, null=True, blank=True)

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
    fecha_modificacion = models.DateTimeField(null=True, blank=True)
    usuario_modificacion = models.CharField(max_length = 203, default='admin')

    
    def __str__(self) -> str:
        return str(self.id) + ' - ' + self.nombre 
    
    def __unicode__(self) -> str:
        return super().__unicode__()

class Sucursal(models.Model):
    nombre = models.CharField(max_length = 30)
    direccion = models.CharField(max_length = 30)
    empresa = models.ForeignKey(Empresa, on_delete = models.CASCADE, blank = True, null = True)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    usuario_creacion = models.CharField(max_length = 203, default='admin')
    fecha_modificacion = models.DateTimeField(auto_now = True)
    usuario_modificacion = models.CharField(max_length = 203, default='admin')

    def __str__(self) -> str:
        return str(self.id) + ' - ' + self.nombre
    
    def __unicode__(self) -> str:
        return super().__unicode__()

class UsuarioManager(BaseUserManager):
    def create_user(self, correo_electronico, password=None, **extra_fields):
        if not correo_electronico:
            raise ValueError("El usuario debe tener un correo electrónico")

        correo_electronico = self.normalize_email(correo_electronico)
        usuario = self.model(correo_electronico=correo_electronico, **extra_fields)
        usuario.set_password(password)  # Cifrar la contraseña
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, correo_electronico, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')
        
        return self.create_user(correo_electronico, password, **extra_fields)
class Usuario(AbstractBaseUser):
    correo_electronico = models.EmailField(unique=True, max_length=100, blank=False, null=False)
    password = models.CharField(max_length=128)  # Aumentar a 128 para almacenar contraseñas cifradas
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    estatus_usuario = models.ForeignKey('EstatusUsuario', on_delete=models.DO_NOTHING, blank=True, null=True, default=0)
    genero = models.ForeignKey('Genero', on_delete=models.DO_NOTHING, blank=True, null=True, default=0)
    ultima_fecha_ingreso = models.DateTimeField(blank=True, null=True)
    intentos_de_acceso = models.IntegerField(default=0)
    ultima_fecha_cambio_password = models.DateTimeField(blank=True, null=True)
    requiere_cambiar_password = models.BooleanField(default=False)
    fotografia = models.CharField(max_length=300, blank=True, null=True)
    telefono_movil = models.CharField(max_length=30, blank=True, null=True)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name="usuarios")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_creacion = models.CharField(max_length=203, default='admin')
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_modificacion = models.CharField(max_length=203, default='admin')
    
    USERNAME_FIELD = 'correo_electronico'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return f"{self.id} - {self.nombre} {self.apellido}"
    
    def get_by_natural_key(self, correo_electronico):
        return self.__class__.objects.get(correo_electronico=correo_electronico)
    
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
    fecha_modificacion = models.DateTimeField(blank = True, null = True)
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
    fecha_modificacion = models.DateTimeField(blank = True, null = True) 
    usuario_modificacion = models.CharField(max_length = 203, blank = True, null = True) 
    
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

class EstadoCivil(models.Model):
    nombre = models.CharField(max_length = 30)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    usuario_creacion = models.CharField(max_length = 203, default='admin')
    fecha_modificacion = models.DateTimeField(auto_now = True)
    usuario_modificacion = models.CharField(max_length = 203, default='admin')
    
    def __str__(self) -> str:
        return str(self.id) + ' - ' + self.nombre
    
    def __unicode__(self) -> str:
        return super().__unicode__()
    
class TipoDocumento(models.Model):
    nombre = models.CharField(max_length = 30)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    usuario_creacion = models.CharField(max_length = 203, default='admin')
    fecha_modificacion = models.DateTimeField(auto_now = True)
    usuario_modificacion = models.CharField(max_length = 203, default='admin')
    
    def __str__(self) -> str:
        return str(self.id) + ' - ' + self.nombre
    
    def __unicode__(self) -> str:
        return super().__unicode__()

class Persona(models.Model):
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    fecha_nacimiento = models.DateField(blank = True, null = True)
    genero = models.ForeignKey(Genero, on_delete = models.DO_NOTHING, blank = True, null = True, default = 0)
    direccion = models.CharField(max_length = 100)
    telefono = models.CharField(max_length = 100)
    correo_electronico = models.CharField(max_length = 100)
    estado_civil = models.ForeignKey(EstadoCivil, on_delete = models.DO_NOTHING, blank = True, null = True, default = 0)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    usuario_creacion = models.CharField(max_length = 203, default='admin')
    fecha_modificacion = models.DateTimeField(null=True, blank=True)
    usuario_modificacion = models.CharField(max_length = 203, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.id)  + ' - ' + self.nombre + ' ' + self.apellido
    
    def __unicode__(self) -> str:
        return super().__unicode__()

class DocumentoPersona(models.Model):
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete = models.DO_NOTHING, blank = True, null = True)
    persona = models.ForeignKey(Persona, on_delete = models.DO_NOTHING, blank = True, null = True)
    numero_documento = models.CharField(max_length = 100)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    usuario_creacion = models.CharField(max_length = 203, default='admin')
    fecha_modificacion = models.DateTimeField(auto_now = True)
    usuario_modificacion = models.CharField(max_length = 203, default='admin')
    
    def __str__(self) -> str:
        return str(self.id)  + ' - ' + str(self.persona) + ' - ' + str(self.tipo_documento)
    
class StatusCuenta(models.Model):
    nombre = models.CharField(max_length = 30)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    usuario_creacion = models.CharField(max_length = 203, default='admin')
    fecha_modificacion = models.DateTimeField(auto_now = True)
    usuario_modificacion = models.CharField(max_length = 203, default='admin')
    
    def __str__(self) -> str:
        return str(self.id) + ' - ' + self.nombre
    
    def __unicode__(self) -> str:
        return super().__unicode__()

class TipoSaldoCuenta(models.Model):
    nombre = models.CharField(max_length = 30)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    usuario_creacion = models.CharField(max_length = 203, default='admin')
    fecha_modificacion = models.DateTimeField(auto_now = True)
    usuario_modificacion = models.CharField(max_length = 203, default='admin')
    
    def __str__(self) -> str:
        return str(self.id) + ' - ' + self.nombre
    
    def __unicode__(self) -> str:
        return super().__unicode__()

class SaldoCuenta(models.Model):
    persona = models.ForeignKey(Persona, on_delete = models.DO_NOTHING, blank = True, null = True)
    status_cuenta = models.ForeignKey(StatusCuenta, on_delete = models.DO_NOTHING, blank = True, null = True)
    tipo_saldo_cuenta = models.ForeignKey(TipoSaldoCuenta, on_delete = models.DO_NOTHING, blank = True, null = True)
    saldo_anterior = models.IntegerField(default = 0)
    debitos = models.IntegerField(default = 0)
    creditos = models.IntegerField(default = 0)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    usuario_creacion = models.CharField(max_length = 203, default='admin')
    fecha_modificacion = models.DateTimeField(auto_now = True)
    usuario_modificacion = models.CharField(max_length = 203, default='admin')

    def __str__(self) -> str:
        return str(self.id) + ' - ' + str(self.persona) + ' - ' + str(self.tipo_saldo_cuenta)
    
    def __unicode__(self) -> str:
        return super().__unicode__()

operacion_cuenta_corriente_choice = {
    (1, "Sumar"),
    (2, "Restar"),
}

class TipoMovimientoCXC(models.Model):
    nombre = models.CharField(max_length = 75)
    operacion_cuenta_corriente = models.IntegerField(default = 1, choices=operacion_cuenta_corriente_choice)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    usuario_creacion = models.CharField(max_length = 203, default='admin')
    fecha_modificacion = models.DateTimeField(auto_now = True)
    usuario_modificacion = models.CharField(max_length = 203, default='admin')
    
    def __str__(self) -> str:
        return str(self.id) + ' - ' + self.nombre
    
    def __unicode__(self) -> str:
        return super().__unicode__()

class MovimientoCuenta(models.Model):
    saldo_cuenta = models.ForeignKey(SaldoCuenta, related_name='saldo_cuenta', on_delete = models.DO_NOTHING, blank = True, null = True)
    tipo_movimiento_cxc = models.ForeignKey(TipoMovimientoCXC, related_name='movimiento_cxc', on_delete = models.DO_NOTHING, blank = True, null = True)    
    fecha_movimiento = models.DateTimeField(auto_now_add = True)
    valor_movimiento = models.IntegerField(default = 0)
    valor_movimiento_pagador = models.IntegerField(default = 0)
    generado_automaticamente = models.BooleanField(default = False)
    descripcion = models.CharField(max_length = 100)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    usuario_creacion = models.CharField(max_length = 203, default='admin')
    fecha_modificacion = models.DateTimeField(auto_now = True)
    usuario_modificacion = models.CharField(max_length = 203, default='admin')
    
    def __str__(self) -> str:
        return str(self.id) + ' - ' + str(self.saldo_cuenta) + ' - ' + str(self.movimiento_cxc)
    
    def __unicode__(self) -> str:
        return super().__unicode__()
