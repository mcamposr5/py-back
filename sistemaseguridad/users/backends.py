# users/backends.py

from django.contrib.auth.backends import ModelBackend
from .models import Usuario

class EmailBackend(ModelBackend):
    def authenticate(self, request, correo_electronico=None, password=None, **kwargs):
        print(f"Autenticando usuario con correo: {correo_electronico}")  # Para verificar que el backend está siendo llamado
        try:
            user = Usuario.objects.get(correo_electronico=correo_electronico)
            if user.check_password(password):
                print("Contraseña correcta.")
                return user
            else:
                print("Contraseña incorrecta.")
        except Usuario.DoesNotExist:
            print("Usuario no encontrado.")
            return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None