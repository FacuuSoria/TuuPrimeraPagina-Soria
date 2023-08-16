from django.apps import AppConfig


class PagwebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pagweb'

    def ready(self):
        # Importa tus modelos aquí para asegurarte de que las aplicaciones estén cargadas
        from .models import Profesor, Alumno, Curso