from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Genero, EstatusUsuario, Empresa, Menu, Opcion, RolOpcion, Sucursal, Rol, Modulo, UsuarioPregunta, UsuarioRol, TipoAcceso, BitacoraAcceso
from .forms import GeneroForm, EstatusUsuarioForm, EmpresaForm, MenuForm, OpcionForm, RolOpcionForm, SucursalForm, RolForm, ModuloForm, UsuarioPreguntaForm, UsuarioRolForm, TipoAccesoForm, BitacoraAccesoForm

def menu_principal(request):
    return render(request, 'menu_principal.html')

def crear_genero(request):
    form = GeneroForm()
     # Obtenemos todos los generos
    listado_generos = Genero.objects.all()
    context = {'form':form,
               'listado_generos': listado_generos, # Pasando la lista de generos al contexto
    }
    return render(request, 'genero.html', context)

@csrf_exempt
def generos(request):
    if request.method == 'POST':
        _id = request.POST.get('id', 0)
        if _id == 0:
            form = GeneroForm(request.POST)
            if not form.is_valid():
                return JsonResponse(form.errors.as_json(), safe = False)
            else:
                genero_nuevo = form.save(commit = True)
                return JsonResponse({'ID':genero_nuevo.id,'Genero':'Creado con exito'}, safe = False)
        else:
            try:
                genero_actual = Genero.objects.get(id = _id)
                form = GeneroForm(request.POST, instance = genero_actual)
                if not form.is_valid():
                    return JsonResponse(form.errors.as_json(), safe = False)
                else:
                    genero_actualizado = form.save(commit = True)
                    return JsonResponse({'ID':genero_actualizado.id,'Genero':'Modificado con exito'}, safe = False)
            except Genero.DoesNotExist:
                return JsonResponse({'Error':'Genero no existe'}, safe = False)
            except:
                return JsonResponse({'Error':'Verifique la informacion'}, safe = False) 
    else:
        id = request.GET.get('id',0)
        if id != 0:
            listado_generos = list(Genero.objects.filter(id = id).values())
        else:
            listado_generos = list(Genero.objects.values())
        return JsonResponse(listado_generos, safe = False)

def crear_estatus_usuario(request):
    form = EstatusUsuarioForm()
    # Obtenemos todos los estados de usuario creados
    listado_estatus_usuario = EstatusUsuario.objects.all()
    context = {'form':form,
               'listado_estatus_usuario': listado_estatus_usuario, # Pasando la lista de estados al contexto
    }
    return render(request, 'estatus_usuario.html', context)
  
@csrf_exempt
def estatus_usuario(request):
    if request.method == 'POST':
        _id = request.POST.get('id', 0)
        if _id == 0: # Crear un nuevo registro
            form = EstatusUsuarioForm(request.POST)
            if form.is_valid():
                estatus_usuario_nuevo = form.save(commit=False)
                estatus_usuario_nuevo.usuario_creacion = request.user # Usuario activo de sesión
                estatus_usuario_nuevo.usuario_modificacion = request.user
                estatus_usuario_nuevo.save()
                #return JsonResponse(form.errors.as_json(), safe = False)
                return JsonResponse({'ID': estatus_usuario_nuevo.id, 'Estado Usuario': 'Creado con exito'}, safe=False)
            else:
                return JsonResponse(form.errors.as_json(), safe=False)
                # Actualziar un registro existente
        else:
            try:
                estatus_usuario_actual = EstatusUsuario.objects.get(id = _id)
                form = EstatusUsuarioForm(request.POST, instance = estatus_usuario_actual)
                if form.is_valid():
                    estatus_usuario_actualizado = form.save(commit=False)
                    estatus_usuario_actualizado.usuario_modificacion = request.user  # Usuario activo
                    estatus_usuario_actualizado.save()
                    #return JsonResponse(form.errors.as_json(), safe = False)
                    return JsonResponse({'ID': estatus_usuario_actualizado.id, 'Estado Usuario': 'Modificado con exito'}, safe=False)
                else:
                    return JsonResponse(form.errors.as_json(), safe=False)
            except EstatusUsuario.DoesNotExist:
                return JsonResponse({'Error':'Estatus usuario no existe'}, safe = False)
            except:
                return JsonResponse({'Error':'Verifique la informacion'}, safe = False) 
    else:
        id = request.GET.get('id',0)
        if id != 0:
            listado_estatus_usuario = list(EstatusUsuario.objects.filter(id = id).values())
        else:
            listado_estatus_usuario = list(EstatusUsuario.objects.values())
        return JsonResponse(listado_estatus_usuario, safe = False)

def crear_empresa(request):
    form = EmpresaForm()
    # Obtenemos todas las empresas creadas
    listado_empresa = Empresa.objects.all()
    context = {
        'form': form,
        'listado_empresa': listado_empresa,  # Pasando la lista de empresas al contexto
    }
    return render(request, 'empresa.html', context)

@csrf_exempt
def empresas(request):
    if request.method == 'POST':
        _id = request.POST.get('id', 0)
        if _id == 0:  # Crear un nuevo registro
            form = EmpresaForm(request.POST)
            if form.is_valid():
                empresa_nueva = form.save(commit=False)
                empresa_nueva.usuario_creacion = request.user  # Usuario activo de sesión
                empresa_nueva.usuario_modificacion = request.user
                empresa_nueva.save()
                return JsonResponse({'ID': empresa_nueva.id, 'Empresa': 'Creado con &eacute;xito'}, safe=False)
            else:
                return JsonResponse(form.errors.as_json(), safe=False)
        else:  # Actualizar un registro existente
            try:
                empresa_actual = Empresa.objects.get(id=_id)
                form = EmpresaForm(request.POST, instance=empresa_actual)
                if form.is_valid():
                    empresa_actualizada = form.save(commit=False)
                    empresa_actualizada.usuario_modificacion = request.user  # Usuario activo
                    empresa_actualizada.save()
                    return JsonResponse({'ID': empresa_actualizada.id, 'Empresa': 'Modificado con &eacute;xito'}, safe=False)
                else:
                    return JsonResponse(form.errors.as_json(), safe=False)
            except Empresa.DoesNotExist:
                return JsonResponse({'Error': 'Empresa no existe'}, safe=False)
            except Exception as e:
                return JsonResponse({'Error': 'Verifique la informacion'}, safe=False)
    else:
        id = request.GET.get('id', 0)
        if id != 0:
            listado_empresas = list(Empresa.objects.filter(id=id).values())
        else:
            listado_empresas = list(Empresa.objects.values())
        return JsonResponse(listado_empresas, safe=False)

def crear_sucursal(request):
    form = SucursalForm()
    # Obtenemos todas las empresas creadas
    listado_sucursal = Sucursal.objects.all()
    listado_empresa = Empresa.objects.all()
    context = {
        'form': form,
        'listado_sucursal': listado_sucursal,
        'listado_empresa': listado_empresa,  # Pasando la lista de empresas al contexto
    }
    return render(request, 'sucursal.html', context)

@csrf_exempt
def sucursales(request):
    if request.method == 'POST':
        _id = request.POST.get('id', 0)
        if _id == 0:  # Crear un nuevo registro
            form = SucursalForm(request.POST)
            if form.is_valid():
                sucursal_nueva = form.save(commit=False)
                sucursal_nueva.usuario_creacion = request.user  # Usuario activo de sesión
                sucursal_nueva.usuario_modificacion = request.user
                sucursal_nueva.save()
                return JsonResponse({'ID': sucursal_nueva.id, 'Sucursal': 'Creado con &eacute;xito'}, safe=False)
            else:
                return JsonResponse(form.errors.as_json(), safe=False)
        else:  # Actualizar un registro existente
            try:
                sucursal_actual = Sucursal.objects.get(id=_id)
                form = SucursalForm(request.POST, instance=sucursal_actual)
                if form.is_valid():
                    sucursal_actualizada = form.save(commit=False)
                    sucursal_actualizada.usuario_modificacion = request.user  # Usuario activo
                    sucursal_actualizada.save()
                    return JsonResponse({'ID': sucursal_actualizada.id, 'Sucursal': 'Modificado con &eacute;xito'}, safe=False)
                else:
                    return JsonResponse(form.errors.as_json(), safe=False)
            except Sucursal.DoesNotExist:
                return JsonResponse({'Error': 'Sucursal no existe'}, safe=False)
            except Exception as e:
                return JsonResponse({'Error': 'Verifique la información'}, safe=False)
    else:
        id = request.GET.get('id', 0)
        if id != 0:
            listado_sucursales = list(Sucursal.objects.filter(id=id).values())
        else:
            listado_sucursales = list(Sucursal.objects.values())
        return JsonResponse(listado_sucursales, safe=False)

def crear_rol(request):
    form = RolForm()
    # Obtenemos todas las empresas creadas
    listado_rol = Rol.objects.all()
    context = {
        'form': form,
        'listado_rol': listado_rol,  # Pasando la lista de empresas al contexto
    }
    return render(request, 'rol.html', context)

@csrf_exempt
def roles(request):
    if request.method == 'POST':
        _id = request.POST.get('id', 0)
        if _id == 0:  # Crear un nuevo rol
            form = RolForm(request.POST)
            if form.is_valid():
                rol_nuevo = form.save(commit=False)
                rol_nuevo.usuario_creacion = request.user  # Usuario activo de sesión
                rol_nuevo.usuario_modificacion = request.user
                rol_nuevo.save()
                return JsonResponse({'ID': rol_nuevo.id, 'Rol': 'Creado con &eacute;xito'}, safe=False)
            else:
                return JsonResponse(form.errors.as_json(), safe=False)
        else:  # Actualizar un rol existente
            try:
                rol_actual = Rol.objects.get(id=_id)
                form = RolForm(request.POST, instance=rol_actual)
                if form.is_valid():
                    rol_actualizado = form.save(commit=False)
                    rol_actualizado.usuario_modificacion = request.user  # Usuario activo
                    rol_actualizado.save()
                    return JsonResponse({'ID': rol_actualizado.id, 'Rol': 'Modificado con &eacute;xito'}, safe=False)
                else:
                    return JsonResponse(form.errors.as_json(), safe=False)
            except Rol.DoesNotExist:
                return JsonResponse({'Error': 'Rol no existe'}, safe=False)
            except Exception as e:
                return JsonResponse({'Error': 'Verifique la información'}, safe=False)
    else:
        id = request.GET.get('id', 0)
        if id != 0:
            listado_roles = list(Rol.objects.filter(id=id).values())
        else:
            listado_roles = list(Rol.objects.values())
        return JsonResponse(listado_roles, safe=False)

@csrf_exempt
def crear_modulo(request):
    form = ModuloForm()
    context = {'form':form}
    return render(request, 'modulo.html', context)

@csrf_exempt
def modulos(request):
    if request.method == 'POST':
        _id = request.POST.get('id', 0)
        if _id == 0:
            form = ModuloForm(request.POST)
            if not form.is_valid():
                return JsonResponse(form.errors.as_json(), safe = False)
            else:
                modulo_nuevo = form.save(commit = True)
                return JsonResponse({'ID':modulo_nuevo.id,'Comentario':'Creado con exito'}, safe = False)
        else:
            try:
                modulo_actual = Modulo.objects.get(id = _id)
                form = ModuloForm(request.POST, instance = modulo_actual)
                if not form.is_valid():
                    return JsonResponse(form.errors.as_json(), safe = False)
                else:
                    modulo_actualizado = form.save(commit = True)
                    return JsonResponse({'ID':modulo_actualizado.id,'Comentario':'Modificado con exito'}, safe = False)
            except Modulo.DoesNotExist:
                return JsonResponse({'Error':'Modulo no existe'}, safe = False)
            except:
                return JsonResponse({'Error':'Verifique la informacion'}, safe = False) 
    else:
        id = request.GET.get('id',0)
        if id != 0:
            listado_modulos = list(Modulo.objects.filter(id = id).values())
        else:
            listado_modulos = list(Modulo.objects.values())
        return JsonResponse(listado_modulos, safe = False)

def crear_menu(request):
    form = MenuForm()
    context = {'form':form}
    return render(request, 'menu.html', context)

@csrf_exempt
def menus(request):
    if request.method == 'POST':
        _id = request.POST.get('id', 0)
        if _id == 0:
            form = MenuForm(request.POST)
            if not form.is_valid():
                return JsonResponse(form.errors.as_json(), safe = False)
            else:
                menu_nuevo = form.save(commit = True)
                return JsonResponse({'ID':menu_nuevo.id,'Comentario':'Creado con exito'}, safe = False)
        else:
            try:
                menu_actual = Menu.objects.get(id = _id)
                form = MenuForm(request.POST, instance = menu_actual)
                if not form.is_valid():
                    return JsonResponse(form.errors.as_json(), safe = False)
                else:
                    menu_actualizado = form.save(commit = True)
                    return JsonResponse({'ID':menu_actualizado.id,'Comentario':'Modificado con exito'}, safe = False)
            except Menu.DoesNotExist:
                return JsonResponse({'Error':'Menu no existe'}, safe = False)
            except:
                return JsonResponse({'Error':'Verifique la informacion'}, safe = False) 
    else:
        id = request.GET.get('id',0)
        if id != 0:
            listado_menus = list(Menu.objects.filter(id = id).values())
        else:
            listado_menus = list(Menu.objects.values())
        return JsonResponse(listado_menus, safe = False)
    
def crear_opcion(request):
    form = OpcionForm()
    context = {'form':form}
    return render(request, 'opcion.html', context)

@csrf_exempt
def opciones(request):
    if request.method == 'POST':
        _id = request.POST.get('id', 0)
        if _id == 0:
            form = OpcionForm(request.POST)
            if not form.is_valid():
                return JsonResponse(form.errors.as_json(), safe = False)
            else:
                opcion_nueva = form.save(commit = True)
                return JsonResponse({'ID':opcion_nueva.id,'Comentario':'Creado con exito'}, safe = False)
        else:
            try:
                opcion_actual = Opcion.objects.get(id = _id)
                form = OpcionForm(request.POST, instance = opcion_actual)
                if not form.is_valid():
                    return JsonResponse(form.errors.as_json(), safe = False)
                else:
                    opcion_actualizada = form.save(commit = True)
                    return JsonResponse({'ID':opcion_actualizada.id,'Comentario':'Modificado con exito'}, safe = False)
            except Opcion.DoesNotExist:
                return JsonResponse({'Error':'Opcion no existe'}, safe = False)
            except:
                return JsonResponse({'Error':'Verifique la informacion'}, safe = False) 
    else:
        id = request.GET.get('id',0)
        if id != 0:
            listado_opciones = list(Opcion.objects.filter(id = id).values())
        else:
            listado_opciones = list(Opcion.objects.values())
        return JsonResponse(listado_opciones, safe = False)

def crear_rol_opcion(request):
    form = RolOpcionForm()
    context = {'form':form}
    return render(request, 'rolopcion.html', context)

@csrf_exempt
def roles_opciones(request):
    if request.method == 'POST':
        _id = request.POST.get('id', 0)
        if _id == 0:
            form = RolOpcionForm(request.POST)
            if not form.is_valid():
                return JsonResponse(form.errors.as_json(), safe = False)
            else:
                rol_opcion_nuevo = form.save(commit = True)
                return JsonResponse({'ID':rol_opcion_nuevo.id,'Comentario':'Creado con exito'}, safe = False)
        else:
            try:
                rol_opcion_actual = RolOpcion.objects.get(id = _id)
                form = RolOpcionForm(request.POST, instance = rol_opcion_actual)
                if not form.is_valid():
                    return JsonResponse(form.errors.as_json(), safe = False)
                else:
                    rol_opcion_actualizado = form.save(commit = True)
                    return JsonResponse({'ID':rol_opcion_actualizado.id,'Comentario':'Modificado con exito'}, safe = False)
            except RolOpcion.DoesNotExist:
                return JsonResponse({'Error':'Rol Opcion no existe'}, safe = False)
            except:
                return JsonResponse({'Error':'Verifique la informacion'}, safe = False) 
    else:
        id = request.GET.get('id',0)
        if id != 0:
            listado_rol_opciones = list(RolOpcion.objects.filter(id = id).values())
        else:
            listado_rol_opciones = list(RolOpcion.objects.values())
        return JsonResponse(listado_rol_opciones, safe = False)
    

def crear_usuario_rol(request):
    form = UsuarioRolForm()
    context = {'form':form}
    return render(request, 'usuariorol.html', context)

@csrf_exempt
def usuarios_roles(request):
    if request.method == 'POST':
        _id = request.POST.get('id', 0)
        if _id == 0:
            form = UsuarioRolForm(request.POST)
            if not form.is_valid():
                return JsonResponse(form.errors.as_json(), safe = False)
            else:
                usuario_rol_nuevo = form.save(commit = True)
                return JsonResponse({'ID':usuario_rol_nuevo.id,'Comentario':'Creado con exito'}, safe = False)
        else:
            try:
                usuario_rol_actual = UsuarioRol.objects.get(id = _id)
                form = UsuarioRolForm(request.POST, instance = usuario_rol_actual)
                if not form.is_valid():
                    return JsonResponse(form.errors.as_json(), safe = False)
                else:
                    usuario_rol_actualizado = form.save(commit = True)
                    return JsonResponse({'ID':usuario_rol_actualizado.id,'Comentario':'Modificado con exito'}, safe = False)
            except UsuarioRol.DoesNotExist:
                return JsonResponse({'Error':'Usuario Rol no existe'}, safe = False)
            except:
                return JsonResponse({'Error':'Verifique la informacion'}, safe = False) 
    else:
        id = request.GET.get('id',0)
        if id != 0:
            listado_usuariosroles = list(UsuarioRol.objects.filter(id = id).values())
        else:
            listado_usuariosroles = list(UsuarioRol.objects.values())
        return JsonResponse(listado_usuariosroles, safe = False)
    

def crear_usuario_pregunta(request):
    form = UsuarioPreguntaForm()
    context = {'form':form}
    return render(request, 'usuariopregunta.html', context)

@csrf_exempt
def usuarios_preguntas(request):
    if request.method == 'POST':
        _id = request.POST.get('id', 0)
        if _id == 0:
            form = UsuarioPreguntaForm(request.POST)
            if not form.is_valid():
                return JsonResponse(form.errors.as_json(), safe = False)
            else:
                usuario_pregunta_nuevo = form.save(commit = True)
                return JsonResponse({'ID':usuario_pregunta_nuevo.id,'Comentario':'Creado con exito'}, safe = False)
        else:
            try:
                usuario_pregunta_actual = UsuarioPregunta.objects.get(id = _id)
                form = UsuarioPreguntaForm(request.POST, instance = usuario_pregunta_actual)
                if not form.is_valid():
                    return JsonResponse(form.errors.as_json(), safe = False)
                else:
                    usuario_pregunta_actualizado = form.save(commit = True)
                    return JsonResponse({'ID':usuario_pregunta_actualizado.id,'Comentario':'Modificado con exito'}, safe = False)
            except UsuarioPregunta.DoesNotExist:
                return JsonResponse({'Error':'Usuario Pregunta no existe'}, safe = False)
            except:
                return JsonResponse({'Error':'Verifique la informacion'}, safe = False) 
    else:
        id = request.GET.get('id',0)
        if id != 0:
            listado_usuariospreguntas = list(UsuarioPregunta.objects.filter(id = id).values())
        else:
            listado_usuariospreguntas = list(UsuarioPregunta.objects.values())
        return JsonResponse(listado_usuariospreguntas, safe = False)
    
@csrf_exempt
def tipo_accesos(request):
    if request.method == 'POST':
        _id = request.POST.get('id', 0)
        if _id == 0:
            form = TipoAccesoForm(request.POST)
            if not form.is_valid():
                return JsonResponse(form.errors.as_json(), safe = False)
            else:
                tipo_acceso_nuevo = form.save(commit = True)
                return JsonResponse({'ID':tipo_acceso_nuevo.id,'Comentario':'Creado con exito'}, safe = False)
        else:
            try:
                tipo_acceso_actual = TipoAcceso.objects.get(id = _id)
                form = TipoAccesoForm(request.POST, instance = tipo_acceso_actual)
                if not form.is_valid():
                    return JsonResponse(form.errors.as_json(), safe = False)
                else:
                    tipo_acceso_actualizado = form.save(commit = True)
                    return JsonResponse({'ID':tipo_acceso_actualizado.id,'Comentario':'Modificado con exito'}, safe = False)
            except TipoAcceso.DoesNotExist:
                return JsonResponse({'Error':'Tipo Acceso no existe'}, safe = False)
            except:
                return JsonResponse({'Error':'Verifique la informacion'}, safe = False) 
    else:
        id = request.GET.get('id',0)
        if id != 0:
            listado_tipoaccesos = list(TipoAcceso.objects.filter(id = id).values())
        else:
            listado_tipoaccesos = list(TipoAcceso.objects.values())
        return JsonResponse(listado_tipoaccesos, safe = False)
    

@csrf_exempt
def bitacora_accesos(request):
    if request.method == 'POST':
        _id = request.POST.get('id', 0)
        if _id == 0:
            form = BitacoraAccesoForm(request.POST)
            if not form.is_valid():
                return JsonResponse(form.errors.as_json(), safe = False)
            else:
                bitacora_acceso_nuevo = form.save(commit = True)
                return JsonResponse({'ID':bitacora_acceso_nuevo.id,'Comentario':'Creado con exito'}, safe = False)
        else:
            try:
                bitacora_acceso_actual = BitacoraAcceso.objects.get(id = _id)
                form = BitacoraAccesoForm(request.POST, instance = bitacora_acceso_actual)
                if not form.is_valid():
                    return JsonResponse(form.errors.as_json(), safe = False)
                else:
                    bitacora_acceso_actualizado = form.save(commit = True)
                    return JsonResponse({'ID':bitacora_acceso_actualizado.id,'Comentario':'Modificado con exito'}, safe = False)
            except BitacoraAcceso.DoesNotExist:
                return JsonResponse({'Error':'Bitacora Acceso no existe'}, safe = False)
            except:
                return JsonResponse({'Error':'Verifique la informacion'}, safe = False) 
    else:
        id = request.GET.get('id',0)
        if id != 0:
            listado_bitacora_accesos = list(BitacoraAcceso.objects.filter(id = id).values())
        else:
            listado_bitacora_accesos = list(BitacoraAcceso.objects.values())
        return JsonResponse(listado_bitacora_accesos, safe = False)