from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.menu_principal, name='menu_principal'),  # Ruta para el menú principal
    path('crear_genero/', views.crear_genero, name='crear_genero'),
    path('generos/', views.generos, name='generos'),
    path('generos/editar/<int:id>/', views.crear_genero, name='genero_editar'),  # Reutilizamos la vista de crear para editar
    path('genero/eliminar/<int:id>/', views.eliminar_genero, name='genero_eliminar'),
    path('crear_estatus_usuario/', views.crear_estatus_usuario, name='crear_estatus_usuario'),
    path('estatus_usuario/', views.estatus_usuario, name='estatus_usuario'),
    path('crear_empresa/', views.crear_empresa, name='crear_empresa'),
    path('empresas/', views.empresas, name='empresas'),
    path('empresas/editar/<int:id>/', views.crear_empresa, name='empresa_editar'), # Reutilizamos la vista de crear para editar
    path('empresas/tienesucursales/<int:id>/', views.empresaTieneSucursales, name='empresa_sucursales'), # Para verificar si la empresa a eliminar tiene sucursales asignadas.
    path('empresa/eliminar/<int:id>/', views.eliminar_empresa, name='empresa_eliminar'),
    path('crear_sucursal/', views.crear_sucursal, name='crear_sucursal'),
    path('sucursales/', views.sucursales, name='sucursales'),
    path('sucursales/editar/<int:id>/', views.crear_sucursal, name='sucursal_editar'),
    path('sucursal/eliminar/<int:id>/', views.eliminar_sucursal, name='sucursal_eliminar'),
    path('crear_rol/', views.crear_rol, name='crear_rol'),
    path('roles/', views.roles, name='roles'),
    path('roles/editar/<int:id>/', views.crear_rol, name='rol_editar'),
    path('rol/eliminar/<int:id>/', views.eliminar_rol, name='rol_eliminar'),    
    path('crear_modulo/', views.crear_modulo, name='crear_modulo'),
    path('modulos/', views.modulos, name='modulos'),
    path('crear_menu/', views.crear_menu, name='crear_menu'),
    path('menus/', views.menus, name='menus'),
    path('crear_opcion/', views.crear_opcion, name='crear_opcion'),
    path('opciones/', views.opciones, name='opciones'),
    path('crear_rol_opcion/', views.crear_rol_opcion, name='crear_rol_opcion'),
    path('roles_opciones/', views.roles_opciones, name='roles_opciones'),
    path('crear_usuario_rol/', views.crear_usuario_rol, name='crear_usuario_rol'),
    path('usuarios_roles/', views.usuarios_roles, name='usuarios_roles'),
    path('crear_usuario_pregunta/', views.crear_usuario_pregunta, name='crear_usuario_pregunta'),
    path('usuarios_preguntas/', views.usuarios_preguntas, name='usuarios_preguntas'),
    path('tipo_accesos/', views.tipo_accesos, name='tipo_accesos'),
    path('bitacora_accessos/', views.bitacora_accesos, name='bitacora_accessos'),
]