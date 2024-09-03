from django.urls import path
from . import views

urlpatterns = [
    path('crear_genero/', views.crear_genero, name='crear_genero'),
    path('generos/', views.generos, name='generos'),
    path('crear_estatus_usuario/', views.crear_estatus_usuario, name='crear_estatus_usuario'),
    path('estatus_usuario/', views.estatus_usuario, name='estatus_usuario'),
    path('crear_empresa/', views.crear_empresa, name='crear_empresa'),
    path('empresas/', views.empresas, name='empresas'),
    path('crear_sucursal/', views.crear_sucursal, name='crear_sucursal'),
    path('sucursales/', views.sucursales, name='sucursales'),
    path('crear_rol/', views.crear_rol, name='crear_rol'),
    path('roles/', views.roles, name='roles'),
    path('crear_modulo/', views.crear_modulo, name='crear_modulo'),
    path('modulos/', views.modulos, name='modulos'),
    path('crear_menu/', views.crear_menu, name='crear_menu'),
    path('menus/', views.menus, name='menus'),
    path('crear_opcion/', views.crear_opcion, name='crear_opcion'),
    path('opciones/', views.opciones, name='opciones'),
    path('crear_rolopcion/', views.crear_rolopcion, name='crear_rolopcion'),
    path('rolesopciones/', views.rolesopciones, name='rolesopciones'),
    path('crear_usuariorol/', views.crear_usuariorol, name='crear_usuariorol'),
    path('usuariosroles/', views.usuariosroles, name='usuariosroles'),
    path('crear_usuariopregunta/', views.crear_usuariopregunta, name='crear_usuariopregunta'),
    path('usuariospreguntas/', views.usuariospreguntas, name='usuariospreguntas'),
]