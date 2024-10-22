from django import forms
from django.forms import ModelForm
from django.core.validators import RegexValidator
from .models import Genero, EstatusUsuario, Empresa, Menu, Opcion, RolOpcion, Sucursal, Rol, Modulo, UsuarioPregunta, UsuarioRol, TipoAcceso, BitacoraAcceso

class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        fields = ['nombre', 'usuario_creacion', 'usuario_modificacion']  # Muestra los campos
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Masculino'}),
            'usuario_creacion': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'usuario_modificacion': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }


class EstatusUsuarioForm(ModelForm):
    # Aplicar el validador de solo letras
    nombre = forms.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z]+$',  # Solo letras
                message='El nombre solo puede contener letras',
                code='invalid_nombre'
            )
        ],
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

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
            'password_cantidad_preguntar_validar', 'usuario_creacion',
            'usuario_modificacion'
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
            'password_cantidad_preguntar_validar': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 5'}),
            'usuario_creacion': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'usuario_modificacion': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super(EmpresaForm, self).__init__(*args, **kwargs)
        # Deshabilitar los campos de usuario
        self.fields['usuario_creacion'].widget.attrs['readonly'] = True
        self.fields['usuario_modificacion'].widget.attrs['readonly'] = True


class SucursalForm(ModelForm):
    class Meta:
        model = Sucursal
        fields = [
            'nombre', 'direccion', 'empresa', 'usuario_creacion',
            'usuario_modificacion'
        ]  # Muestra los campos
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Mi Sucursal'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 9av. 5-30 zona 4. San José Pinula, San José Pinula, Guatemala'}),
            'empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'usuario_creacion': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'usuario_modificacion': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super(SucursalForm, self).__init__(*args, **kwargs)
        # Deshabilitar los campos de usuario
        self.fields['usuario_creacion'].widget.attrs['readonly'] = True
        self.fields['usuario_modificacion'].widget.attrs['readonly'] = True


class RolForm(ModelForm):
    class Meta:
        model = Rol
        fields = [
            'nombre', 'usuario_creacion',
            'usuario_modificacion'
        ]  # Muestra los campos
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Administrador'}),
            'usuario_creacion': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'usuario_modificacion': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super(RolForm, self).__init__(*args, **kwargs)
        # Deshabilitar los campos de usuario
        self.fields['usuario_creacion'].widget.attrs['readonly'] = True
        self.fields['usuario_modificacion'].widget.attrs['readonly'] = True


class ModuloForm(ModelForm):
    class Meta:
        model = Modulo
        fields = '__all__'


class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'


class OpcionForm(ModelForm):
    class Meta:
        model = Opcion
        fields = '__all__'


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
