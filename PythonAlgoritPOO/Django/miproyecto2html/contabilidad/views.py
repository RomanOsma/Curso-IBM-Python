# views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import date
from .models import Cliente, Factura
from django import forms


# Vista para mostrar un saludo
def saludo(request):
    texto = """
    <html>
        <head>
            <title>Saludo</title>
        </head>
        <body>
            <h1>Hola, este es un saludo desde Django</h1>
            <h2>saludo desde Django h2</h2>
            <p>Este es un párrafo</p>
        </body>
    </html>"""
    return HttpResponse(texto)

# Vista para mostrar la fecha actual
def fecha(request):
    miFecha = date.today()  # Obtiene la fecha actual
    texto2 = """
    <html>
    <body>
    <h2>Fecha y hora actual: </h2>%s
    </body>
    </html>
    """ % miFecha
    return HttpResponse(texto2)

# Vista para calcular la edad futura
def calcEdad(request, year):
    edadActual = 40
    periodo = year - 2025
    edadFutura = edadActual + periodo
    documento = "<html><body><h2>En el año %s tendrás %s años.</h2></body></html>" % (year, edadFutura)
    return HttpResponse(documento)

# Vista para calcular la edad futura con una edad inicial dada
def calcEdad2(request, edadActual, year):
    periodo = year - 2025
    edadFutura = edadActual + periodo
    documento = "<html><body><h2>En el año %s tendrás %s años.</h2></body></html>" % (year, edadFutura)
    return HttpResponse(documento)

"""
# Vista para crear un cliente y una factura (solo para demostración)
def crear_cliente(request):
    # Verificar si el cliente ya existe
    rfc = "AGRM-801205-400"
    if Cliente.objects.filter(rfc=rfc).exists():
        return HttpResponse("El cliente ya existe en la base de datos.")

    # Crear el cliente si no existe
    fecha_nacimiento = date(1980, 12, 5)
    pedro = Cliente(
        nombre="Pedro",
        apellidos="Aguilar Ramírez",
        rfc=rfc,
        fecha_nacimiento=fecha_nacimiento,
        activo=True,
    )
    pedro.save()

    # Crear la factura asociada al cliente
    factura = Factura(cliente=pedro, importe=5690.12, pagada=False)
    factura.save()

    # Usando el método create()
    pedro = Cliente.objects.create(
        nombre="Angel",
        apellidos="Martin Ramírez",
        rfc="AGRM-801410-987",
        fecha_nacimiento=fecha_nacimiento,
        activo=True,
    )
    factura = Factura.objects.create(cliente=pedro, importe=9999.99, pagada=False)

    return HttpResponse("Cliente y factura creados exitosamente.")
"""
# views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import date
from .models import Cliente, Factura
from django import forms

# Definimos un formulario para Cliente
class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=50, label="Nombre")
    apellidos = forms.CharField(max_length=100, label="Apellidos")
    rfc = forms.CharField(max_length=15, label="RFC")
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de Nacimiento")
    activo = forms.BooleanField(required=False, initial=True, label="Activo")
    
    # Campo opcional para crear factura
    crear_factura = forms.BooleanField(required=False, initial=False, label="Crear factura")
    importe_factura = forms.DecimalField(max_digits=10, decimal_places=2, required=False, label="Importe de factura")
    factura_pagada = forms.BooleanField(required=False, initial=False, label="Factura pagada")

# Vista modificada para usar el formulario
def crear_cliente(request):
    if request.method == 'POST':
        # Procesamos el formulario enviado
        form = ClienteForm(request.POST)
        if form.is_valid():
            # Obtenemos los datos validados
            datos = form.cleaned_data
            
            # Verificamos si el cliente ya existe
            if Cliente.objects.filter(rfc=datos['rfc']).exists():
                return HttpResponse(f"Error: Ya existe un cliente con el RFC {datos['rfc']}.")
            
            # Creamos el cliente
            cliente = Cliente.objects.create(
                nombre=datos['nombre'],
                apellidos=datos['apellidos'],
                rfc=datos['rfc'],
                fecha_nacimiento=datos['fecha_nacimiento'],
                activo=datos['activo']
            )
            
            # Si se marcó la opción de crear factura y se proporcionó un importe
            mensaje = f"Cliente {cliente.nombre} {cliente.apellidos} creado exitosamente."
            if datos['crear_factura'] and datos['importe_factura']:
                factura = Factura.objects.create(
                    cliente=cliente,
                    importe=datos['importe_factura'],
                    pagada=datos['factura_pagada']
                )
                mensaje += f" Factura por {factura.importe}€ creada."
            
            return HttpResponse(mensaje)
    else:
        # Mostramos el formulario vacío
        form = ClienteForm()
    
    # Renderizamos la plantilla con el formulario
    return render(request, 'crear_cliente.html', {'form': form})