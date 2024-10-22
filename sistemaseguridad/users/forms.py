from django import forms
from django.forms import ModelForm
from django.core.validators import RegexValidator
from .models import DocumentoPersona, EstadoCivil, EstatusCuenta, Genero, EstatusUsuario, Empresa, Menu, MovimientoCuenta, Opcion, Persona, RolOpcion, SaldoCuenta, Sucursal, Rol, Modulo, TipoDocumento, TipoMovimientoCXC, TipoSaldoCuenta, UsuarioPregunta, UsuarioRol, TipoAcceso, BitacoraAcceso

class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        fields = '__all__'
        fields = ['nombre', 'usuario_creacion', 'usuario_modificacion']  # Muestra los campos
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Masculino'}),
            'usuario_creacion': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'usuario_modificacion': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }


class EstatusUsuarioForm(ModelForm):

    class EstatusUsuarioForm(forms.ModelForm):
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
        fields = '__all__'

class SucursalForm(ModelForm):
    class Meta:
        model = Sucursal
        fields = '__all__'

class RolForm(ModelForm):
    class Meta:
        model = Rol
        fields = '__all__'

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
