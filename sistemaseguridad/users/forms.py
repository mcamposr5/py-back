from django import forms
from django.forms import ModelForm
from .models import DocumentoPersona, EstadoCivil, EstatusCuenta, Genero, EstatusUsuario, Empresa, Menu, MovimientoCuenta, Opcion, Persona, RolOpcion, SaldoCuenta, Sucursal, Rol, Modulo, TipoDocumento, TipoMovimientoCXC, TipoSaldoCuenta, UsuarioPregunta, UsuarioRol, TipoAcceso, BitacoraAcceso

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
        fields = '__all__'
    
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
