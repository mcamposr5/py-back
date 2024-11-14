from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('home/', views.menu_principal, name='menu_principal'),  # Ruta para el menú principal
    path('crear_genero/', views.crear_genero, name='crear_genero'),
    path('generos/', views.generos, name='generos'),
    path('generos/editar/<int:id>/', views.crear_genero, name='genero_editar'),  # Reutilizamos la vista de crear para editar
    path('genero/eliminar/<int:id>/', views.eliminar_genero, name='genero_eliminar'),

    path('crear_estatus_usuario/', views.crear_estatus_usuario, name='crear_estatus_usuario'),
    path('estatus_usuario/', views.estatus_usuario, name='estatus_usuario'),
    path('estatus_usuario/editar/<int:id>/', views.crear_estatus_usuario, name='editar_estatus'),  # Reutilizamos la vista de crear para editar
    path('estatus_usuario/eliminar/<int:id>/', views.eliminar_estatus_usuario, name='eliminar_estatus'),


    path('crear_empresa/', views.crear_empresa, name='crear_empresa'),
    path('empresas/', views.empresas, name='empresas'),
    path('empresas/editar/<int:id>/', views.crear_empresa, name='empresa_editar'), # Reutilizamos la vista de crear para editar
    path('empresas/tienesucursales/<int:id>/', views.empresaTieneSucursales, name='empresa_sucursales'), # Para verificar si la empresa a eliminar tiene sucursales asignadas.
    path('empresa/search_nombre/', views.empresa_search_nombre, name='empresa_search_nombre'),
    path('empresa/eliminar/<int:id>/', views.eliminar_empresa, name='empresa_eliminar'),
    path('crear_sucursal/', views.crear_sucursal, name='crear_sucursal'),
    path('sucursales/', views.sucursales, name='sucursales'),
    path('sucursales/editar/<int:id>/', views.crear_sucursal, name='sucursal_editar'),
    path('sucursal/eliminar/<int:id>/', views.eliminar_sucursal, name='sucursal_eliminar'),
    path('sucursal/search_nombre/', views.sucursal_search_nombre, name='sucursal_search_nombre'),
    path('crear_rol/', views.crear_rol, name='crear_rol'),
    path('roles/', views.roles, name='roles'),
    path('crear_modulo/', views.crear_modulo, name='crear_modulo'),
    path('modulos/', views.modulos, name='modulos'),
    path('crear_menu/', views.crear_menu, name='crear_menu'),
    path('menus/', views.crear_menu, name='menus'),
    path('menus/editar/<int:id>/', views.crear_menu, name='menu_editar'),
    path('menu/eliminar/<int:id>/', views.eliminar_menu, name='menu_eliminar'),
    path('crear_modulo/', views.crear_modulo, name='crear_modulo'),
    path('modulos/', views.crear_modulo, name='modulos'),
    path('modulos/editar/<int:id>/', views.crear_modulo, name='modulo_editar'),
    path('modulo/eliminar/<int:id>/', views.eliminar_modulo, name='modulo_eliminar'),
    path('crear_opcion/', views.crear_opcion, name='crear_opcion'),
    path('opciones/', views.crear_opcion, name='opciones'),
    path('opciones/editar/<int:id>/', views.crear_opcion, name='opcion_editar'),
    path('opcion/eliminar/<int:id>/', views.eliminar_opcion, name='opcion_eliminar'),
    path('crear_rol_opcion/', views.crear_rol_opcion, name='crear_rol_opcion'),
    path('roles_opciones/', views.roles_opciones, name='roles_opciones'),
    path('crear_usuario_rol/', views.crear_usuario_rol, name='crear_usuario_rol'),
    path('usuarios_roles/', views.usuarios_roles, name='usuarios_roles'),
    path('crear_usuario_pregunta/', views.crear_usuario_pregunta, name='crear_usuario_pregunta'),
    path('usuarios_preguntas/', views.usuarios_preguntas, name='usuarios_preguntas'),
    path('crear_tipo_acceso/', views.crear_tipo_acceso, name='crear_tipo_acceso'),
    path('tipoacceso/editar/<int:id>/', views.crear_tipo_acceso, name='tipoacceso_editar'),
    path('tipoacceso/eliminar/<int:id>/', views.eliminar_tipoacceso, name='tipoacceso_eliminar'),
    path('tipo_accesos/', views.tipo_accesos, name='tipo_accesos'),
    path('bitacora_accesos/', views.bitacora_accesos, name='bitacora_accesos'),

    path('crear_estado_civil/', views.crear_estado_civil, name='crear_estado_civil'),
    path('estados_civiles/', views.estados_civiles, name='estados_civiles'),
    path('estados_civiles/editar/<int:id>/', views.crear_estado_civil, name='estado_civil_editar'), 
    path('estado_civil/eliminar/<int:id>/', views.eliminar_estado_civil, name='estado_civil_eliminar'),
    path('crear_tipo_documento/', views.crear_tipo_documento, name='crear_tipo_documento'),
    path('tipos_documentos/', views.tipos_documentos, name='tipos_documentos'),
    path('tipos_documentos/editar/<int:id>/', views.crear_tipo_documento, name='tipo_documento_editar'), 
    path('tipo_documento/eliminar/<int:id>/', views.eliminar_tipo_documento, name='tipo_documento_eliminar'),
    path('crear_persona/', views.crear_persona, name='crear_persona'),
    path('personas/', views.personas, name='personas'),
    path('personas/editar/<int:id>/', views.crear_persona, name='persona_editar'), 
    path('persona/eliminar/<int:id>/', views.eliminar_persona, name='persona_eliminar'),

    path('crear_documento_persona/', views.crear_documento_persona, name='crear_documento_persona'),
    path('documento_persona/', views.crear_documento_persona, name='documento_persona'),
    path('documento_persona/editar/<int:id>/', views.crear_documento_persona, name='editar_documento_persona'),
    path('documento_persona/eliminar', views.eliminar_documento_persona, name='eliminar_documento_persona'),

    path('crear_status_cuenta/', views.crear_status_cuenta, name='crear_status_cuenta'),
    path('status_cuenta/', views.crear_status_cuenta, name='status_cuenta'),
    path('status_cuenta/eliminar', views.eliminar_status_cuenta, name='eliminar_status_cuenta'),

    path('crear_tipo_saldo_cuenta/', views.crear_tipo_saldo_cuenta, name='crear_tipo_saldo_cuenta'),
    path('tipo_saldo_cuenta/', views.crear_tipo_saldo_cuenta, name='tipo_saldo_cuenta'),
    path('tipo_saldo_cuenta/eliminar/', views.eliminar_tipo_saldo_cuenta, name='eliminar_tipo_saldo_cuenta'),
    path('crear_saldo_cuenta/', views.saldos_cuentas, name='crear_saldo_cuenta'),
    path('saldo_cuenta/eliminar/', views.eliminar_saldo_cuenta, name='eliminar_saldo_cuenta'),
    path('crear_tipo_movimiento_cxc/', views.tipos_movimientos_cxc, name='crear_tipo_movimiento_cxc'),
    path('tipo_movimiento_cxc/eliminar/', views.eliminar_tipo_movimiento_cxc, name='eliminar_tipo_movimiento_cxc'),
    path('movimiento_cuenta/', views.movimiento_cuentas, name='movimiento_cuenta'),
    path('movimiento_cuenta/eliminar/', views.eliminar_movimiento_cuenta, name='eliminar_movimiento_cuenta'),
    path('cierre_mes', views.cierre_mes, name='cierre_mes'),
    path('tipo_saldo_cuenta/editar/<int:id>/', views.crear_tipo_saldo_cuenta, name='editar_tipo_saldo_cuenta'),
    path('tipo_saldo_cuenta/eliminar/<int:id>/', views.eliminar_tipo_saldo_cuenta, name='eliminar_tipo_saldo_cuenta'),
    
    path('usuarios/', views.usuarios, name='usuarios'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/editar/<int:id>/', views.crear_usuario, name='editar_usuario'),
    path('usuario/eliminar/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),

    path('administracion/', views.administracion, name='administracion'), 
    path('cuenta_corriente/', views.cuenta_corriente, name='cuenta_corriente'), 
    path('estado_civil/', views.crear_estado_civil, name='estado_civil'), 

    #Agrupación de rutas modulo login
    path('login/', views.login_view, name='login'),
    path('cambiar_password/', views.cambiar_password, name='cambiar_password'),
    path('verificar_preguntas/', views.verificar_preguntas, name='verificar_preguntas'),
    path('recuperar_password/', views.solicitar_correo, name='solicitar_correo'),
    path('logout/', views.logout_view, name='logout'),
    path('bitacora_accesos/search/', views.bitacora_accesos_search, name='bitacora_accesos_search'), 
    path('bitacora_accesos/searchuser/', views.bitacora_accesos_search_user, name='bitacora_accesos_search_user'),    
]