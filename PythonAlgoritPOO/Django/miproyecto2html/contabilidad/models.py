from django.db import models

# Create your models here.
from django.db import models

# Modelo Cliente: Representa a un cliente en la base de datos
class Cliente(models.Model):
    nombre = models.CharField(max_length=64)  # Campo para el nombre del cliente
    apellidos = models.CharField(max_length=64)  # Campo para los apellidos del cliente
    rfc = models.CharField(max_length=15, unique=True)  # RFC único para cada cliente
    fecha_nacimiento = models.DateField()  # Fecha de nacimiento del cliente
    activo = models.BooleanField(default=True)  # Indica si el cliente está activo o no

    # Método para representar el objeto como una cadena
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

# Modelo Factura: Representa una factura asociada a un cliente
class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Relación con el modelo Cliente
    importe = models.DecimalField(max_digits=8, decimal_places=2)  # Importe de la factura
    pagada = models.BooleanField(default=False)  # Indica si la factura está pagada o no

    # Método para representar el objeto como una cadena
    def __str__(self):
        return f"Factura {self.id} - {self.cliente.nombre}"