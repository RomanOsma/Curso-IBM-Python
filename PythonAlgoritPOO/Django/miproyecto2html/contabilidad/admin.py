from django.contrib import admin
from .models import Cliente, Factura

# Registra los modelos en el panel de administración
admin.site.register(Cliente)
admin.site.register(Factura)