<<<<<<< HEAD
import os
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
=======
"""
Configuración ASGI para el proyecto config.

Expone el objeto invocable ASGI como una variable a nivel de módulo llamada ``application``.

Para más información sobre este archivo, consulta
https://docs.djangoproject.com/en/6.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

>>>>>>> origin/main
application = get_asgi_application()
