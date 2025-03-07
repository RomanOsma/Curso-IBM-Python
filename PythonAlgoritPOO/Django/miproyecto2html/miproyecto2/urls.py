"""
URL configuration for miproyecto2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contabilidad.views import saludo, fecha, calcEdad, calcEdad2, crear_cliente

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para el panel de administración de Django
    path('saludo', saludo),  # URL para la vista de saludo
    path('fecha', fecha),  # URL para la vista de fecha
    path('calcEdad/<int:year>', calcEdad),  # URL para calcular la edad futura
    path('calcEdad2/<int:edadActual>/<int:year>', calcEdad2),  # URL para calcular la edad futura con edad inicial
    path('crear_cliente', crear_cliente),  # URL para crear un cliente y una factura
]