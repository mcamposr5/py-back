from django.utils import timezone
from django.shortcuts import redirect
from datetime import timedelta
from users.models import BitacoraAcceso  # Importa el modelo donde se guarda la bitácora

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Define el tiempo de inactividad en minutos
        session_timeout = 5  # 5 minutos

        # Verificar si el usuario está autenticado
        if request.user.is_authenticated:
            last_activity = request.session.get('last_activity')
            current_time = timezone.now()

            # Si no se encuentra la última actividad, se inicializa
            if not last_activity:
                request.session['last_activity'] = current_time.isoformat()
            else:
                # Calcula el tiempo de inactividad
                last_activity = timezone.datetime.fromisoformat(last_activity)
                inactivity_period = current_time - last_activity

                # Si el tiempo de inactividad supera el límite, cierra la sesión
                if inactivity_period > timedelta(minutes=session_timeout):
                    # Actualizar el registro en BitacoraAcceso para marcar la sesión como "INACTIVA"
                    try:
                        bitacora = BitacoraAcceso.objects.filter(usuario=request.user, sesion="ACTIVA").last()
                        if bitacora:
                            bitacora.sesion = "INACTIVA"
                            bitacora.save()
                    except BitacoraAcceso.DoesNotExist:
                        pass

                    # Cierra la sesión del usuario y redirige al login
                    from django.contrib.auth import logout
                    logout(request)
                    return redirect('login')

                # Actualiza la última actividad de la sesión
                request.session['last_activity'] = current_time.isoformat()

        response = self.get_response(request)
        return response