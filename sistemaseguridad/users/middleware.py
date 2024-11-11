from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Lista de rutas exentas de autenticación
        self.exempt_urls = [
            reverse('login'),
            reverse('logout'),
            reverse('solicitar_correo'),
            reverse('verificar_preguntas'),
            reverse('cambiar_password')
        ]

    def __call__(self, request):
        # Verificar si el usuario no está autenticado y si la URL actual no está exenta
        if not request.user.is_authenticated and not any(request.path.startswith(url) for url in self.exempt_urls):
            return redirect('login')
        
        return self.get_response(request)