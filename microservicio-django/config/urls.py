<<<<<<< HEAD
from django.urls import include, path
urlpatterns = [path('api/', include('catalogo.urls'))]
=======
"""
Configuración de URL para el proyecto config.

La lista `urlpatterns` dirige las URL hacia las vistas. Para más información consulta:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Ejemplos:
Vistas basadas en funciones
    1. Agrega un import:  from my_app import views
    2. Agrega una URL a urlpatterns:  path('', views.home, name='home')
Vistas basadas en clases
    1. Agrega un import:  from other_app.views import Home
    2. Agrega una URL a urlpatterns:  path('', Home.as_view(), name='home')
Incluir otro URLconf
    1. Importa la función include(): from django.urls import include, path
    2. Agrega una URL a urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("catalogo.urls")),
]
>>>>>>> origin/main
