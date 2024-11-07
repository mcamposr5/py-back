from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from .models import DocumentoPersona, EstadoCivil, EstatusCuenta, Genero, EstatusUsuario, Empresa, Menu, MovimientoCuenta, Opcion, Persona, RolOpcion, SaldoCuenta, Sucursal, Rol, Modulo, TipoDocumento, TipoMovimientoCXC, TipoSaldoCuenta, UsuarioPregunta, UsuarioRol, TipoAcceso, BitacoraAcceso
from .forms import DocumentoPersonaForm, EstadoCivilForm, EstatusCuentaForm, GeneroForm, EstatusUsuarioForm, EmpresaForm, MenuForm, MovimientoCuentaForm, OpcionForm, PersonaForm, RolOpcionForm, SaldoCuentaForm, SucursalForm, RolForm, ModuloForm, TipoDocumentoForm, TipoMovimientoCXCForm, TipoSaldoCuentaForm, UsuarioPreguntaForm, UsuarioRolForm, TipoAccesoForm, BitacoraAccesoForm

def menu_principal(request):
    return render(request, 'menu_principal.html')

def crear_genero(request, id=None):
    if request.method == 'POST':
        if id:  # Si estamos editando
            genero = get_object_or_404(Genero, id=id)
            form = GeneroForm(request.POST, instance=genero)
            mensaje = 'Género actualizado con éxito'

            if form.is_valid():
                # Actualizamos usuario_modificacion y fecha_modificacion al editar
                genero = form.save(commit=False)
                genero.fecha_modificacion = timezone.now()  # Fecha y hora de la modificación
                genero.usuario_modificacion = request.user.username  # Usuario que hace la modificación
                genero.save()
                return JsonResponse({'success': True, 
                                     'nombre': genero.nombre, 
                                     'usuario_modificacion': genero.usuario_modificacion,
                                     'mensaje': mensaje})

        else:  # Si estamos creando uno nuevo
            form = GeneroForm(request.POST)
            mensaje = 'Género creado con éxito'
            if form.is_valid():
                # Al crear, asignamos usuario_creacion pero no usuario_modificacion
                genero = form.save(commit=False)
                genero.usuario_creacion = request.user.username # Usuario que crea el género
                genero.save()
                return JsonResponse({'success': True, 
                                     'nombre': genero.nombre, 
                                     'usuario_creacion': genero.usuario_creacion,
                                     'mensaje': mensaje})

        return JsonResponse({'success': False, 'errors': form.errors.as_json()}, status=400)

    listado_generos = Genero.objects.all()
    form = GeneroForm()
    context = {'form': form, 'listado_generos': listado_generos}
    return render(request, 'genero.html', context)

@csrf_exempt
def eliminar_genero(request, id):
    if request.method == 'POST':
        try:
            genero = Genero.objects.get(id=id)
            genero.delete()
            return JsonResponse({'message': 'Género eliminado con éxito.'}, status=200)
        except Genero.DoesNotExist:
            return JsonResponse({'error': 'El género no existe.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': 'Ocurrió un error.'}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido.'}, status=405)

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

def crear_modulo(request, id=None):
    if request.method == 'POST':
        if id:
            modulo = get_object_or_404(Modulo, id=id)
            form = ModuloForm(request.POST, instance=modulo)
            mensaje = 'Módulo actualizado con éxito'

            if form.is_valid():
                modulo = form.save(commit=False)
                modulo.fecha_modificacion = timezone.now()
                modulo.usuario_modificacion = request.user.username
                modulo.save()
                return JsonResponse({
                    'success': True,
                    'nombre': modulo.nombre,
                    'orden_menu': modulo.orden_menu,
                    'usuario_modificacion': modulo.usuario_modificacion,
                    'mensaje': mensaje
                })

        else:
            form = ModuloForm(request.POST)
            mensaje = 'Módulo creado con éxito'
            if form.is_valid():
                modulo = form.save(commit=False)
                modulo.usuario_creacion = request.user.username
                modulo.save()
                return JsonResponse({
                    'success': True,
                    'nombre': modulo.nombre,
                    'orden_menu': modulo.orden_menu,
                    'usuario_creacion': modulo.usuario_creacion,
                    'mensaje': mensaje
                })

        return JsonResponse({'success': False, 'errors': form.errors.as_json()}, status=400)

    listado_modulos = Modulo.objects.all()
    form = ModuloForm()
    context = {'form': form, 'listado_modulos': listado_modulos}
    return render(request, 'modulo.html', context)

@csrf_exempt
def eliminar_modulo(request, id):
    if request.method == 'POST':
        try:
            modulo = Modulo.objects.get(id=id)
            modulo.delete()
            return JsonResponse({'message': 'Módulo eliminado con éxito.'}, status=200)
        except Modulo.DoesNotExist:
            return JsonResponse({'error': 'El módulo no existe.'}, status=404)
        except Exception:
            return JsonResponse({'error': 'Ocurrió un error.'}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido.'}, status=405)

@csrf_exempt
def modulos(request):
    if request.method == 'POST':
        _id = request.POST.get('id', 0)
        if _id == 0:
            form = ModuloForm(request.POST)
            if not form.is_valid():
                return JsonResponse(form.errors.as_json(), safe=False)
            else:
                modulo_nuevo = form.save(commit=True)
                return JsonResponse({'ID': modulo_nuevo.id, 'Modulo': 'Creado con éxito'}, safe=False)
        else:
            try:
                modulo_actual = Modulo.objects.get(id=_id)
                form = ModuloForm(request.POST, instance=modulo_actual)
                if not form.is_valid():
                    return JsonResponse(form.errors.as_json(), safe=False)
                else:
                    modulo_actualizado = form.save(commit=True)
                    return JsonResponse({'ID': modulo_actualizado.id, 'Modulo': 'Modificado con éxito'}, safe=False)
            except Modulo.DoesNotExist:
                return JsonResponse({'Error': 'El módulo no existe'}, safe=False)
            except:
                return JsonResponse({'Error': 'Verifique la información'}, safe=False)
    else:
        id = request.GET.get('id', 0)
        listado_modulos = list(Modulo.objects.filter(id=id).values()) if id else list(Modulo.objects.values())
        return JsonResponse(listado_modulos, safe=False)



def crear_menu(request, id=None):
    if request.method == 'POST':
        if id:  # Si estamos editando
            menu = get_object_or_404(Menu, id=id)
            form = MenuForm(request.POST, instance=menu)
            mensaje = 'Menú actualizado con éxito'

            if form.is_valid():
                menu = form.save(commit=False)
                menu.fecha_modificacion = timezone.now()
                menu.usuario_modificacion = request.user.username
                menu.save()
                return JsonResponse({
                    'success': True,
                    'nombre': menu.nombre,
                    'modulo': menu.modulo.nombre if menu.modulo else None,
                    'orden_menu': menu.orden_menu,
                    'usuario_modificacion': menu.usuario_modificacion,
                    'mensaje': mensaje
                })

        else:  # Si estamos creando uno nuevo
            form = MenuForm(request.POST)
            mensaje = 'Menú creado con éxito'
            if form.is_valid():
                menu = form.save(commit=False)
                menu.usuario_creacion = request.user.username
                menu.save()
                return JsonResponse({
                    'success': True,
                    'nombre': menu.nombre,
                    'modulo': menu.modulo.nombre if menu.modulo else None,
                    'orden_menu': menu.orden_menu,
                    'usuario_creacion': menu.usuario_creacion,
                    'mensaje': mensaje
                })

        return JsonResponse({'success': False, 'errors': form.errors.as_json()}, status=400)

    listado_menus = Menu.objects.all()
    form = MenuForm()
    context = {'form': form, 'listado_menus': listado_menus}
    return render(request, 'menu.html', context)

@csrf_exempt
def eliminar_menu(request, id):
    if request.method == 'POST':
        try:
            menu = Menu.objects.get(id=id)
            menu.delete()
            return JsonResponse({'message': 'Menú eliminado con éxito.'}, status=200)
        except Menu.DoesNotExist:
            return JsonResponse({'error': 'El menú no existe.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': 'Ocurrió un error.'}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido.'}, status=405)

@csrf_exempt
def menus(request):
    if request.method == 'POST':
        _id = request.POST.get('id', 0)
        if _id == 0:  # Creación
            form = MenuForm(request.POST)
            if not form.is_valid():
                return JsonResponse(form.errors.as_json(), safe=False)
            else:
                menu_nuevo = form.save(commit=True)
                return JsonResponse({'ID': menu_nuevo.id, 'Menu': 'Creado con éxito'}, safe=False)
        else:  # Edición
            try:
                menu_actual = Menu.objects.get(id=_id)
                form = MenuForm(request.POST, instance=menu_actual)
                if not form.is_valid():
                    return JsonResponse(form.errors.as_json(), safe=False)
                else:
                    menu_actualizado = form.save(commit=True)
                    return JsonResponse({'ID': menu_actualizado.id, 'Menu': 'Modificado con éxito'}, safe=False)
            except Menu.DoesNotExist:
                return JsonResponse({'Error': 'El menú no existe'}, safe=False)
            except:
                return JsonResponse({'Error': 'Verifique la información'}, safe=False)
    else:
        id = request.GET.get('id', 0)
        listado_menus = list(Menu.objects.filter(id=id).values()) if id else list(Menu.objects.values())
        return JsonResponse(listado_menus, safe=False)


    
def crear_opcion(request, id=None):
    if request.method == 'POST':
        if id:
            opcion = get_object_or_404(Opcion, id=id)
            form = OpcionForm(request.POST, instance=opcion)
            mensaje = 'Opción actualizada con éxito'

            if form.is_valid():
                opcion = form.save(commit=False)
                opcion.fecha_modificacion = timezone.now()
                opcion.usuario_modificacion = request.user.username
                opcion.save()
                return JsonResponse({
                    'success': True,
                    'nombre': opcion.nombre,
                    'menu': opcion.menu.nombre if opcion.menu else None,
                    'orden_menu': opcion.orden_menu,
                    'usuario_modificacion': opcion.usuario_modificacion,
                    'mensaje': mensaje
                })

        else:
            form = OpcionForm(request.POST)
            mensaje = 'Opción creada con éxito'
            if form.is_valid():
                opcion = form.save(commit=False)
                opcion.usuario_creacion = request.user.username
                opcion.save()
                return JsonResponse({
                    'success': True,
                    'nombre': opcion.nombre,
                    'menu': opcion.menu.nombre if opcion.menu else None,
                    'orden_menu': opcion.orden_menu,
                    'usuario_creacion': opcion.usuario_creacion,
                    'mensaje': mensaje
                })

        return JsonResponse({'success': False, 'errors': form.errors.as_json()}, status=400)

    listado_opciones = Opcion.objects.all()
    form = OpcionForm()
    context = {'form': form, 'listado_opciones': listado_opciones}
    return render(request, 'opcion.html', context)

@csrf_exempt
def eliminar_opcion(request, id):
    if request.method == 'POST':
        try:
            opcion = Opcion.objects.get(id=id)
            opcion.delete()
            return JsonResponse({'message': 'Opción eliminada con éxito.'}, status=200)
        except Opcion.DoesNotExist:
            return JsonResponse({'error': 'La opción no existe.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': 'Ocurrió un error.'}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido.'}, status=405)

@csrf_exempt
def opciones(request):
    if request.method == 'POST':
        _id = request.POST.get('id', 0)
        if _id == 0:
            form = OpcionForm(request.POST)
            if not form.is_valid():
                return JsonResponse(form.errors.as_json(), safe=False)
            else:
                opcion_nueva = form.save(commit=True)
                return JsonResponse({'ID': opcion_nueva.id, 'Opcion': 'Creada con éxito'}, safe=False)
        else:
            try:
                opcion_actual = Opcion.objects.get(id=_id)
                form = OpcionForm(request.POST, instance=opcion_actual)
                if not form.is_valid():
                    return JsonResponse(form.errors.as_json(), safe=False)
                else:
                    opcion_actualizada = form.save(commit=True)
                    return JsonResponse({'ID': opcion_actualizada.id, 'Opcion': 'Modificada con éxito'}, safe=False)
            except Opcion.DoesNotExist:
                return JsonResponse({'Error': 'La opción no existe'}, safe=False)
            except:
                return JsonResponse({'Error': 'Verifique la información'}, safe=False)
    else:
        id = request.GET.get('id', 0)
        listado_opciones = list(Opcion.objects.filter(id=id).values()) if id else list(Opcion.objects.values())
        return JsonResponse(listado_opciones, safe=False)


    
def crear_rol_opcion(request):
    form = RolOpcionForm()
    listado_rol_opcion = RolOpcion.objects.all()
    context = {
        'form':form,
        'listado_rol_opcion': listado_rol_opcion,
        }
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
    listado_usuario_rol = UsuarioRol.objects.all()
    context = {
        'form':form,
        'listado_usuario_rol': listado_usuario_rol,
        }

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

def crear_estado_civil(request, id=None):
    if request.method == 'POST':
        if id:  # Editar Estado Civil
            estado_civil = get_object_or_404(EstadoCivil, id=id)
            form = EstadoCivilForm(request.POST, instance=estado_civil)
            mensaje = 'Estado Civil actualizado con éxito'

            if form.is_valid():
                estado_civil = form.save(commit=False)
                estado_civil.fecha_modificacion = timezone.now()
                estado_civil.usuario_modificacion = request.user.username
                estado_civil.save()
                return JsonResponse({'success': True, 
                                     'nombre': estado_civil.nombre, 
                                     'usuario_modificacion': estado_civil.usuario_modificacion,
                                     'mensaje': mensaje})

        else:  # Crear nuevo Estado Civil
            form = EstadoCivilForm(request.POST)
            mensaje = 'Estado Civil creado con éxito'
            if form.is_valid():
                estado_civil = form.save(commit=False)
                estado_civil.usuario_creacion = request.user.username
                estado_civil.save()
                return JsonResponse({'success': True, 
                                     'nombre': estado_civil.nombre, 
                                     'usuario_creacion': estado_civil.usuario_creacion,
                                     'mensaje': mensaje})

        return JsonResponse({'success': False, 'errors': form.errors.as_json()}, status=400)

    listado_estados_civiles = EstadoCivil.objects.all()
    form = EstadoCivilForm()
    context = {'form': form, 'listado_estados_civiles': listado_estados_civiles}
    return render(request, 'estados_civiles.html', context)

@csrf_exempt
def eliminar_estado_civil(request, id):
    if request.method == 'POST':
        try:
            estado_civil = EstadoCivil.objects.get(id=id)
            estado_civil.delete()
            return JsonResponse({'message': 'Estado Civil eliminado con éxito.'}, status=200)
        except EstadoCivil.DoesNotExist:
            return JsonResponse({'error': 'El Estado Civil no existe.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': 'Ocurrió un error.'}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido.'}, status=405)

@csrf_exempt
def estados_civiles(request):
    if request.method == 'POST':
        _id = request.POST.get('id', 0)
        if _id == 0:  # Crear
            form = EstadoCivilForm(request.POST)
            if not form.is_valid():
                return JsonResponse(form.errors.as_json(), safe=False)
            else:
                estado_civil_nuevo = form.save(commit=True)
                return JsonResponse({'ID': estado_civil_nuevo.id, 'EstadoCivil': 'Creado con éxito'}, safe=False)
        else:  # Editar
            try:
                estado_civil_actual = EstadoCivil.objects.get(id=_id)
                form = EstadoCivilForm(request.POST, instance=estado_civil_actual)
                if not form.is_valid():
                    return JsonResponse(form.errors.as_json(), safe=False)
                else:
                    estado_civil_actualizado = form.save(commit=True)
                    return JsonResponse({'ID': estado_civil_actualizado.id, 'EstadoCivil': 'Modificado con éxito'}, safe=False)
            except EstadoCivil.DoesNotExist:
                return JsonResponse({'Error': 'Estado Civil no existe'}, safe=False)
            except:
                return JsonResponse({'Error': 'Verifique la información'}, safe=False)
    else:
        id = request.GET.get('id', 0)
        if id != 0:
            listado_estados_civiles = list(EstadoCivil.objects.filter(id=id).values())
        else:
            listado_estados_civiles = list(EstadoCivil.objects.values())
        return JsonResponse(listado_estados_civiles, safe=False)

    
    
def crear_tipo_documento(request, id=None):
    if request.method == 'POST':
        if id:  # Editar Tipo Documento
            tipo_documento = get_object_or_404(TipoDocumento, id=id)
            form = TipoDocumentoForm(request.POST, instance=tipo_documento)
            mensaje = 'Tipo de Documento actualizado con éxito'

            if form.is_valid():
                tipo_documento = form.save(commit=False)
                tipo_documento.fecha_modificacion = timezone.now()
                tipo_documento.usuario_modificacion = request.user.username
                tipo_documento.save()
                return JsonResponse({'success': True, 
                                     'nombre': tipo_documento.nombre, 
                                     'usuario_modificacion': tipo_documento.usuario_modificacion,
                                     'mensaje': mensaje})

        else:  # Crear nuevo Tipo Documento
            form = TipoDocumentoForm(request.POST)
            mensaje = 'Tipo de Documento creado con éxito'
            if form.is_valid():
                tipo_documento = form.save(commit=False)
                tipo_documento.usuario_creacion = request.user.username
                tipo_documento.save()
                return JsonResponse({'success': True, 
                                     'nombre': tipo_documento.nombre, 
                                     'usuario_creacion': tipo_documento.usuario_creacion,
                                     'mensaje': mensaje})

        return JsonResponse({'success': False, 'errors': form.errors.as_json()}, status=400)

    listado_tipos_documentos = TipoDocumento.objects.all()
    form = TipoDocumentoForm()
    context = {'form': form, 'listado_tipos_documentos': listado_tipos_documentos}
    return render(request, 'tipos_documentos.html', context)

@csrf_exempt
def eliminar_tipo_documento(request, id):
    if request.method == 'POST':
        try:
            tipo_documento = TipoDocumento.objects.get(id=id)
            tipo_documento.delete()
            return JsonResponse({'message': 'Tipo de Documento eliminado con éxito.'}, status=200)
        except TipoDocumento.DoesNotExist:
            return JsonResponse({'error': 'El Tipo de Documento no existe.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': 'Ocurrió un error.'}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido.'}, status=405)

@csrf_exempt
def tipos_documentos(request):
    if request.method == 'POST':
        _id = request.POST.get('id', 0)
        if _id == 0:  # Crear
            form = TipoDocumentoForm(request.POST)
            if not form.is_valid():
                return JsonResponse(form.errors.as_json(), safe=False)
            else:
                tipo_documento_nuevo = form.save(commit=True)
                return JsonResponse({'ID': tipo_documento_nuevo.id, 'TipoDocumento': 'Creado con éxito'}, safe=False)
        else:  # Editar
            try:
                tipo_documento_actual = TipoDocumento.objects.get(id=_id)
                form = TipoDocumentoForm(request.POST, instance=tipo_documento_actual)
                if not form.is_valid():
                    return JsonResponse(form.errors.as_json(), safe=False)
                else:
                    tipo_documento_actualizado = form.save(commit=True)
                    return JsonResponse({'ID': tipo_documento_actualizado.id, 'TipoDocumento': 'Modificado con éxito'}, safe=False)
            except TipoDocumento.DoesNotExist:
                return JsonResponse({'Error': 'Tipo de Documento no existe'}, safe=False)
            except:
                return JsonResponse({'Error': 'Verifique la información'}, safe=False)
    else:
        id = request.GET.get('id', 0)
        if id != 0:
            listado_tipos_documentos = list(TipoDocumento.objects.filter(id=id).values())
        else:
            listado_tipos_documentos = list(TipoDocumento.objects.values())
        return JsonResponse(listado_tipos_documentos, safe=False)

    
def crear_persona(request, id=None):
    if request.method == 'POST':
        if id:  # Editar Persona existente
            persona = get_object_or_404(Persona, id=id)
            form = PersonaForm(request.POST, instance=persona)
            mensaje = 'Persona actualizada con éxito'

            if form.is_valid():
                persona = form.save(commit=False)
                persona.fecha_modificacion = timezone.now()
                persona.usuario_modificacion = request.user.username
                persona.save()
                return JsonResponse({
                    'success': True,
                    'nombre': persona.nombre,
                    'apellido': persona.apellido,
                    'usuario_modificacion': persona.usuario_modificacion,
                    'mensaje': mensaje
                })

        else:  # Crear nueva Persona
            form = PersonaForm(request.POST)
            mensaje = 'Persona creada con éxito'
            if form.is_valid():
                persona = form.save(commit=False)
                persona.usuario_creacion = request.user.username
                persona.save()
                return JsonResponse({
                    'success': True,
                    'nombre': persona.nombre,
                    'apellido': persona.apellido,
                    'usuario_creacion': persona.usuario_creacion,
                    'mensaje': mensaje
                })

        return JsonResponse({'success': False, 'errors': form.errors.as_json()}, status=400)

    # Renderizar el formulario y la lista de personas
    listado_personas = Persona.objects.all()
    estados_civiles = EstadoCivil.objects.all()
    generos = Genero.objects.all()
    tipos_documentos = TipoDocumento.objects.all()
    form = PersonaForm()
    context = {
        'form': form,
        'listado_personas': listado_personas,
        'estados_civiles': estados_civiles,
        'generos': generos,
        'tipos_documentos': tipos_documentos,
    }
    return render(request, 'personas.html', context)


@csrf_exempt
def eliminar_persona(request, id):
    if request.method == 'POST':
        try:
            persona = Persona.objects.get(id=id)
            persona.delete()
            return JsonResponse({'message': 'Persona eliminada con éxito.'}, status=200)
        except Persona.DoesNotExist:
            return JsonResponse({'error': 'La Persona no existe.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': 'Ocurrió un error.'}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido.'}, status=405)


@csrf_exempt
def personas(request):
    if request.method == 'POST':
        _id = request.POST.get('id', 0)
        if _id == 0:  # Crear nueva Persona
            form = PersonaForm(request.POST)
            if not form.is_valid():
                return JsonResponse(form.errors.as_json(), safe=False)
            else:
                persona_nueva = form.save(commit=True)
                return JsonResponse({'ID': persona_nueva.id, 'Persona': 'Creado con éxito'}, safe=False)
        else:  # Editar Persona existente
            try:
                persona_actual = Persona.objects.get(id=_id)
                form = PersonaForm(request.POST, instance=persona_actual)
                if not form.is_valid():
                    return JsonResponse(form.errors.as_json(), safe=False)
                else:
                    persona_actualizada = form.save(commit=True)
                    return JsonResponse({'ID': persona_actualizada.id, 'Persona': 'Modificado con éxito'}, safe=False)
            except Persona.DoesNotExist:
                return JsonResponse({'Error': 'Persona no existe'}, safe=False)
            except Exception as e:
                return JsonResponse({'Error': 'Verifique la información'}, safe=False)
    else:
        # Obtener una persona específica o la lista completa
        id = request.GET.get('id', 0)
        if id != 0:
            listado_personas = list(Persona.objects.filter(id=id).values(
                'id', 'nombre', 'apellido', 'fecha_nacimiento', 'genero__nombre', 'direccion', 
                'telefono', 'correo_electronico', 'estado_civil__nombre', 'tipo_documento__nombre',
                'usuario_creacion', 'usuario_modificacion', 'fecha_creacion', 'fecha_modificacion'))
        else:
            listado_personas = list(Persona.objects.values(
                'id', 'nombre', 'apellido', 'fecha_nacimiento', 'genero__nombre', 'direccion', 
                'telefono', 'correo_electronico', 'estado_civil__nombre', 'tipo_documento__nombre',
                'usuario_creacion', 'usuario_modificacion', 'fecha_creacion', 'fecha_modificacion'))
        return JsonResponse(listado_personas, safe=False)
    
@csrf_exempt
def documentos_personas(request):
    if request.method == 'POST':
        _id = request.POST.get('id', 0)
        if _id == 0:
            form = DocumentoPersonaForm(request.POST)
            if not form.is_valid():
                return JsonResponse(form.errors.as_json(), safe = False)
            else:
                documento_persona_nuevo = form.save(commit = True)
                return JsonResponse({'ID':documento_persona_nuevo.id,'Comentario':'Creado con exito'}, safe = False)
        else:
            try:
                documento_persona_actual = DocumentoPersona.objects.get(id = _id)
                form = DocumentoPersonaForm(request.POST, instance = documento_persona_actual)
                if not form.is_valid():
                    return JsonResponse(form.errors.as_json(), safe = False)
                else:
                    documento_persona_actualizado = form.save(commit = True)
                    return JsonResponse({'ID':documento_persona_actualizado.id,'Comentario':'Modificado con exito'}, safe = False)
            except DocumentoPersona.DoesNotExist:
                return JsonResponse({'Error':'Documento Persona no existe'}, safe = False)
            except:
                return JsonResponse({'Error':'Verifique la informacion'}, safe = False) 
    else:
        id = request.GET.get('id',0)
        if id != 0:
            listado_documentos_personas = list(DocumentoPersona.objects.filter(id = id).values())
        else:
            listado_documentos_personas = list(DocumentoPersona.objects.values())
        return JsonResponse(listado_documentos_personas, safe = False)
    
@csrf_exempt
def estatus_cuentas(request):
    if request.method == 'POST':
        _id = request.POST.get('id', 0)
        if _id == 0:
            form = EstatusCuentaForm(request.POST)
            if not form.is_valid():
                return JsonResponse(form.errors.as_json(), safe = False)
            else:
                estatus_cuenta_nuevo = form.save(commit = True)
                return JsonResponse({'ID':estatus_cuenta_nuevo.id,'Comentario':'Creado con exito'}, safe = False)
        else:
            try:
                estatus_cuenta_actual = EstatusCuenta.objects.get(id = _id)
                form = EstatusCuentaForm(request.POST, instance = estatus_cuenta_actual)
                if not form.is_valid():
                    return JsonResponse(form.errors.as_json(), safe = False)
                else:
                    estatus_cuenta_actualizado = form.save(commit = True)
                    return JsonResponse({'ID':estatus_cuenta_actualizado.id,'Comentario':'Modificado con exito'}, safe = False)
            except EstatusCuenta.DoesNotExist:
                return JsonResponse({'Error':'Estatus Cuenta no existe'}, safe = False)
            except:
                return JsonResponse({'Error':'Verifique la informacion'}, safe = False) 
    else:
        id = request.GET.get('id',0)
        if id != 0:
            listado_estatus_cuentas = list(EstatusCuenta.objects.filter(id = id).values())
        else:
            listado_estatus_cuentas = list(EstatusCuenta.objects.values())
        return JsonResponse(listado_estatus_cuentas, safe = False)

@csrf_exempt
def tipos_saldo_cuentas(request):
    if request.method == 'POST':
        _id = request.POST.get('id', 0)
        if _id == 0:
            form = TipoSaldoCuentaForm(request.POST)
            if not form.is_valid():
                return JsonResponse(form.errors.as_json(), safe = False)
            else:
                tipo_saldo_cuenta_nuevo = form.save(commit = True)
                return JsonResponse({'ID':tipo_saldo_cuenta_nuevo.id,'Comentario':'Creado con exito'}, safe = False)
        else:
            try:
                tipo_saldo_cuenta_actual = TipoSaldoCuenta.objects.get(id = _id)
                form = TipoSaldoCuentaForm(request.POST, instance = tipo_saldo_cuenta_actual)
                if not form.is_valid():
                    return JsonResponse(form.errors.as_json(), safe = False)
                else:
                    tipo_saldo_cuenta_actualizado = form.save(commit = True)
                    return JsonResponse({'ID':tipo_saldo_cuenta_actualizado.id,'Comentario':'Modificado con exito'}, safe = False)
            except TipoSaldoCuenta.DoesNotExist:
                return JsonResponse({'Error':'Tipo Saldo Cuenta no existe'}, safe = False)
            except:
                return JsonResponse({'Error':'Verifique la informacion'}, safe = False) 
    else:
        id = request.GET.get('id',0)
        if id != 0:
            listado_tipos_saldo_cuentas = list(TipoSaldoCuenta.objects.filter(id = id).values())
        else:
            listado_tipos_saldo_cuentas = list(TipoSaldoCuenta.objects.values())
        return JsonResponse(listado_tipos_saldo_cuentas, safe = False)

@csrf_exempt
def saldos_cuentas(request):
    if request.method == 'POST':
        _id = request.POST.get('id', 0)
        if _id == 0:
            form = SaldoCuentaForm(request.POST)
            if not form.is_valid():
                return JsonResponse(form.errors.as_json(), safe = False)
            else:
                saldo_cuenta_nuevo = form.save(commit = True)
                return JsonResponse({'ID':saldo_cuenta_nuevo.id,'Comentario':'Creado con exito'}, safe = False)
        else:
            try:
                saldo_cuenta_actual = SaldoCuenta.objects.get(id = _id)
                form = SaldoCuentaForm(request.POST, instance = saldo_cuenta_actual)
                if not form.is_valid():
                    return JsonResponse(form.errors.as_json(), safe = False)
                else:
                    saldo_cuenta_actualizado = form.save(commit = True)
                    return JsonResponse({'ID':saldo_cuenta_actualizado.id,'Comentario':'Modificado con exito'}, safe = False)
            except SaldoCuenta.DoesNotExist:
                return JsonResponse({'Error':'Saldo Cuenta no existe'}, safe = False)
            except:
                return JsonResponse({'Error':'Verifique la informacion'}, safe = False) 
    else:
        id = request.GET.get('id',0)
        if id != 0:
            listado_saldos_cuentas = list(SaldoCuenta.objects.filter(id = id).values())
        else:
            listado_saldos_cuentas = list(SaldoCuenta.objects.values())
        return JsonResponse(listado_saldos_cuentas, safe = False)

@csrf_exempt
def tipos_movimientos_cxc(request):
    if request.method == 'POST':
        _id = request.POST.get('id', 0)
        if _id == 0:
            form = TipoMovimientoCXCForm(request.POST)
            if not form.is_valid():
                return JsonResponse(form.errors.as_json(), safe = False)
            else:
                tipo_movimiento_cxc_nuevo = form.save(commit = True)
                return JsonResponse({'ID':tipo_movimiento_cxc_nuevo.id,'Comentario':'Creado con exito'}, safe = False)
        else:
            try:
                tipo_movimiento_cxc_actual = TipoMovimientoCXC.objects.get(id = _id)
                form = TipoMovimientoCXCForm(request.POST, instance = tipo_movimiento_cxc_actual)
                if not form.is_valid():
                    return JsonResponse(form.errors.as_json(), safe = False)
                else:
                    tipo_movimiento_cxc_actualizado = form.save(commit = True)
                    return JsonResponse({'ID':tipo_movimiento_cxc_actualizado.id,'Comentario':'Modificado con exito'}, safe = False)
            except TipoMovimientoCXC.DoesNotExist:    
                return JsonResponse({'Error':'Tipo Movimiento CXC no existe'}, safe = False)
            except:
                return JsonResponse({'Error':'Verifique la informacion'}, safe = False) 
    else:
        id = request.GET.get('id',0)
        if id != 0:
            listado_tipos_movimientos_cxc = list(TipoMovimientoCXC.objects.filter(id = id).values())
        else:
            listado_tipos_movimientos_cxc = list(TipoMovimientoCXC.objects.values())
        return JsonResponse(listado_tipos_movimientos_cxc, safe = False)

@csrf_exempt
def movimiento_cuentas(request):
    if request.method == 'POST':
        _id = request.POST.get('id', 0)
        if _id == 0:
            form = MovimientoCuentaForm(request.POST)
            if not form.is_valid():
                return JsonResponse(form.errors.as_json(), safe = False)
            else:
                movimiento_cxc_nuevo = form.save(commit = True)
                return JsonResponse({'ID':movimiento_cxc_nuevo.id,'Comentario':'Creado con exito'}, safe = False)
        else:
            try:
                movimiento_cxc_actual = MovimientoCuenta.objects.get(id = _id)
                form = MovimientoCuentaForm(request.POST, instance = movimiento_cxc_actual)
                if not form.is_valid():
                    return JsonResponse(form.errors.as_json(), safe = False)
                else:
                    movimiento_cxc_actualizado = form.save(commit = True)
                    return JsonResponse({'ID':movimiento_cxc_actualizado.id,'Comentario':'Modificado con exito'}, safe = False)
            except MovimientoCuenta.DoesNotExist:
                return JsonResponse({'Error':'Movimiento Cuenta no existe'}, safe = False)
            except:
                return JsonResponse({'Error':'Verifique la informacion'}, safe = False) 
    else:
        id = request.GET.get('id',0)
        if id != 0:
            listado_movimientos_cxc = list(MovimientoCuenta.objects.filter(id = id).values())
        else:
            listado_movimientos_cxc = list(MovimientoCuenta.objects.values())
        return JsonResponse(listado_movimientos_cxc, safe = False)