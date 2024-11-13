from django import forms
from django.forms import ModelForm
from django.core.validators import RegexValidator
from .models import DocumentoPersona, EstadoCivil, StatusCuenta, Genero, EstatusUsuario, Empresa, Menu, MovimientoCuenta, Opcion, Persona, RolOpcion, SaldoCuenta, Sucursal, Rol, Modulo, TipoDocumento, TipoMovimientoCXC, TipoSaldoCuenta, UsuarioPregunta, UsuarioRol, TipoAcceso, BitacoraAcceso

class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        fields = ['nombre']  # Muestra los campos
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Masculino'}),
        }


class EstatusUsuarioForm(ModelForm):
    # Definir el campo `nombre` sin el validador de solo letras
    nombre = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = EstatusUsuario
        fields = ['nombre'] 

    class Meta:
        model = EstatusUsuario
        fields = ['nombre', 'usuario_creacion', 'usuario_modificacion']  # Muestra los campos
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Activo'}),
            'usuario_creacion': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'usuario_modificacion': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super(EstatusUsuarioForm, self).__init__(*args, **kwargs)
        # Deshabilitar los campos de usuario
        self.fields['usuario_creacion'].widget.attrs['readonly'] = True
        self.fields['usuario_modificacion'].widget.attrs['readonly'] = True


class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = [
            'nombre', 'direccion', 'nit', 'password_cantidad_mayusculas',
            'password_cantidad_minusculas', 'password_cantidad_caracteres_especiales',
            'password_cantidad_caducidad_dias', 'password_cantidad_numeros',
            'password_tamano', 'password_intentos_antes_de_bloquear',
            'password_cantidad_preguntar_validar'
        ]  # Muestra los campos
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Mi Empresa'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 9av. 5-30 zona 4. San José Pinula, San José Pinula, Guatemala'}),
            'nit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 3684015230101'}),
            'password_cantidad_mayusculas': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 5'}),
            'password_cantidad_minusculas': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 5'}),
            'password_cantidad_caracteres_especiales': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 5'}),
            'password_cantidad_caducidad_dias': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 5'}),
            'password_cantidad_numeros': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 5'}),
            'password_tamano': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 5'}),
            'password_intentos_antes_de_bloquear': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 5'}),
            'password_cantidad_preguntar_validar': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 5'})
        }


class SucursalForm(ModelForm):
    class Meta:
        model = Sucursal
        fields = [
            'nombre', 'direccion', 'empresa'
        ]  # Muestra los campos
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Mi Sucursal'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 9av. 5-30 zona 4. San José Pinula, San José Pinula, Guatemala'})
            # 'empresa': forms.TextInput(attrs={'class': 'form-control'}),
        }

class RolForm(ModelForm):
    class Meta:
        model = Rol
        fields = [
            'nombre'
        ]  # Muestra los campos
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Administrador'})
        }

    def __init__(self, *args, **kwargs):
        super(RolForm, self).__init__(*args, **kwargs)
        # Deshabilitar los campos de usuario
        # self.fields['usuario_creacion'].widget.attrs['readonly'] = True
        # self.fields['usuario_modificacion'].widget.attrs['readonly'] = True

class ModuloForm(forms.ModelForm):
    class Meta:
        model = Modulo
        fields = ['nombre', 'orden_menu']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del módulo'}),
            'orden_menu': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 1'}),
        }


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['modulo', 'nombre', 'orden_menu']
        widgets = {
            'modulo': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del menú'}),
            'orden_menu': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 1'}),
        }


class OpcionForm(forms.ModelForm):
    class Meta:
        model = Opcion
        fields = ['menu', 'nombre', 'pagina', 'orden_menu', 'pagina']
        widgets = {
            'menu': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de la opción'}),
            'orden_menu': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 1'}),
            'pagina': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la url'}),
        }


       
class RolOpcionForm(ModelForm):
    class Meta:
        model = RolOpcion
        fields = '__all__'


class UsuarioRolForm(ModelForm):
    class Meta:
        model = UsuarioRol
        fields = '__all__'


class UsuarioPreguntaForm(ModelForm):
    class Meta:
        model = UsuarioPregunta
        fields = '__all__'


class TipoAccesoForm(ModelForm):
    class Meta:
        model = TipoAcceso
        fields = [
            'nombre'
        ]  # Muestra los campos
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Master'})
        }


class BitacoraAccesoForm(ModelForm):
    class Meta:
        model = BitacoraAcceso
        fields = '__all__'

class EstadoCivilForm(forms.ModelForm):
    class Meta:
        model = EstadoCivil
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del estado civil'}),
        }

class TipoDocumentoForm(forms.ModelForm):
    class Meta:
        model = TipoDocumento
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del tipo de documento'}),
        }

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombre', 
            'apellido', 
            'fecha_nacimiento', 
            'genero', 
            'direccion', 
            'telefono', 
            'correo_electronico', 
            'estado_civil'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el apellido'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la dirección'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el teléfono'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el correo electrónico'}),
            'estado_civil': forms.Select(attrs={'class': 'form-control'}),
        }
        
class DocumentoPersonaForm(forms.ModelForm):
    class Meta:
        model = DocumentoPersona
        fields = ['numero_documento', 'tipo_documento', 'persona']  # Usar los campos existentes
        widgets = {
            'numero_documento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número del documento'}),
            'tipo_documento': forms.Select(attrs={'class': 'form-control'}),
            'persona': forms.Select(attrs={'class': 'form-control'}),
        }



class StatusCuentaForm(forms.ModelForm):
    class Meta:
        model = StatusCuenta  # Cambiar de 'StatusCuenta' a 'StatusCuenta'
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del status cuenta'}),
        }


class TipoSaldoCuentaForm(forms.ModelForm):
    class Meta:
        model = TipoSaldoCuenta
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo de saldo de cuenta'}),
        }

class SaldoCuentaForm(ModelForm):
    class Meta:
        model = SaldoCuenta
        fields = [
            'persona', 
            'status_cuenta', 
            'tipo_saldo_cuenta',
            'saldo_anterior',
            'debitos', 
            'creditos'
        ]
        widgets = {
            'persona': forms.Select(attrs={'class': 'form-control'}),
            'status_cuenta': forms.Select(attrs={'class': 'form-control'}),
            'tipo_saldo_cuenta': forms.Select(attrs={'class': 'form-control'}),
            'saldo_anterior': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 0, 'type': 'number', 'step': '0.01'}),
            'debitos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 0, 'type': 'number', 'step': '0.01'}),
            'creditos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 0, 'type': 'number', 'step': '0.01'})
        }

class TipoMovimientoCXCForm(ModelForm):
    class Meta:
        model = TipoMovimientoCXC
        fields = [
            'nombre', 
            'operacion_cuenta_corriente'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del tipo de movimiento'}),
            'operacion_cuenta_corriente': forms.Select(attrs={'class': 'form-control'})
        }

class MovimientoCuentaForm(ModelForm):
    class Meta:
        model = MovimientoCuenta
        fields = [
            'saldo_cuenta', 
            'tipo_movimiento_cxc', 
            'fecha_movimiento',
            'valor_movimiento',
            'valor_movimiento_pagado', 
            'generado_automaticamente',
            'descripcion'
        ]
        widgets = {
            'saldo_cuenta': forms.Select(attrs={'class': 'form-control'}),
            'tipo_movimiento_cxc': forms.Select(attrs={'class': 'form-control'}),
            'fecha_movimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'valor_movimiento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 0, 'type': 'number', 'step': '0.01'}),
            'valor_movimiento_pagado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 0, 'type': 'number', 'step': '0.01'}),
            'generado_automaticamente': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la descripcion del movimiento de cuenta'}),
        }

