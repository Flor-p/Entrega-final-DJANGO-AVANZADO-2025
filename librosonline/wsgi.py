import os
import sys

# Agregamos al path la carpeta que contiene el proyecto
project_path = '/var/www/librosonline'
if project_path not in sys.path:
    sys.path.append(project_path)

# Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'librosonline.settings')

# Aplicación WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
