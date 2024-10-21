from django import forms
from django.forms import ModelForm
from .models import Genero, EstatusUsuario, Empresa, Menu, Opcion, RolOpcion, Sucursal, Rol, Modulo, UsuarioPregunta, UsuarioRol, TipoAcceso, BitacoraAcceso

class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        fields = '__all__'
        # exclude = ('archivado',)

    #  def __init__(self, *args, **kwargs):
    #     super(ProductoForm, self).__init__(*args, **kwargs)
    #     self.fields['categoria_producto'].queryset = CategoriaProducto.objects.filter(archivado = False)
    #     self.fields['moneda'].queryset = Moneda.objects.filter(archivado = False)
    #     self.fields['cobro'].queryset = Cobro.objects.filter(archivado = False)

class EstatusUsuarioForm(ModelForm):
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
            'modulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Activo'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Activo'}),
            'orden_menu': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Activo'}),
            'usuario_creacion': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'usuario_modificacion': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
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
        'menu': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Activo'}),
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