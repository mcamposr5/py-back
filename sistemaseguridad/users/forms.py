from django import forms
from django.forms import ModelForm
from django.core.validators import RegexValidator
from .models import DocumentoPersona, EstadoCivil, EstatusCuenta, Genero, EstatusUsuario, Empresa, Menu, MovimientoCuenta, Opcion, Persona, RolOpcion, SaldoCuenta, Sucursal, Rol, Modulo, TipoDocumento, TipoMovimientoCXC, TipoSaldoCuenta, UsuarioPregunta, UsuarioRol, TipoAcceso, BitacoraAcceso

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

class ModuloForm(ModelForm):
    class Meta:
        model = Modulo
        fields = ['nombre','orden_menu', 'usuario_creacion', 'usuario_modificacion']  # Muestra los campos
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Activo'}),
            'orden_menu': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Activo'}),
            'usuario_creacion': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'usuario_modificacion': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
        def __init__(self, *args, **kwargs):
            super(ModuloForm, self).__init__(*args, **kwargs)
            # Deshabilitar los campos de usuario
            self.fields['usuario_creacion'].widget.attrs['readonly'] = True
            self.fields['usuario_modificacion'].widget.attrs['readonly'] = True


class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = ['modulo','nombre','orden_menu', 'usuario_creacion', 'usuario_modificacion']  # Muestra los campos
        widgets = {
            # 'modulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Activo'}),
            # 'modulo': forms.ModelChoiceField(queryset=Modulo.objects.all(), required=True, help_text='Elija el modulo', label='Modulo', to_field_name='nombre'),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Activo'}),
            'orden_menu': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Activo'}),
            'usuario_creacion': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'default': 'admin'}),
            'usuario_modificacion': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'default': 'admin'}),
        }
        def __init__(self, *args, **kwargs):
            super(MenuForm, self).__init__(*args, **kwargs)
        # Deshabilitar los campos de usuario
            self.fields['usuario_creacion'].widget.attrs['readonly'] = True
            self.fields['usuario_modificacion'].widget.attrs['readonly'] = True


class OpcionForm(ModelForm):
    class Meta:
        model = Opcion
        fields = ['menu','nombre','orden_menu', 'usuario_creacion', 'usuario_modificacion']  # Muestra los campos
        widgets = {
        #'menu': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Activo'}),
        'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Activo'}),
        'orden_menu': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Activo'}),
        'usuario_creacion': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        'usuario_modificacion': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
        def __init__(self, *args, **kwargs):
            super(OpcionForm, self).__init__(*args, **kwargs)
        # Deshabilitar los campos de usuario
            self.fields['usuario_creacion'].widget.attrs['readonly'] = True
            self.fields['usuario_modificacion'].widget.attrs['readonly'] = True


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
        fields = '__all__'


class BitacoraAccesoForm(ModelForm):
    class Meta:
        model = BitacoraAcceso
        fields = '__all__'

class EstadoCivilForm(ModelForm):
    class Meta:
        model = EstadoCivil
        fields = '__all__'

class TipoDocumentoForm(ModelForm):
    class Meta:
        model = TipoDocumento
        fields = '__all__'

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

class DocumentoPersonaForm(ModelForm):
    class Meta:
        model = DocumentoPersona
        fields = '__all__'

class EstatusCuentaForm(ModelForm):
    class Meta:
        model = EstatusCuenta
        fields = '__all__'

class TipoSaldoCuentaForm(ModelForm):
    class Meta:
        model = TipoSaldoCuenta
        fields = '__all__'

class SaldoCuentaForm(ModelForm):
    class Meta:
        model = SaldoCuenta
        fields = '__all__'
    
class TipoMovimientoCXCForm(ModelForm):
    class Meta:
        model = TipoMovimientoCXC
        fields = '__all__'

class MovimientoCuentaForm(ModelForm):
    class Meta:
        model = MovimientoCuenta
        fields = '__all__'

