

# Crea una clase base llamada Dispositivo con un método encender que 
# devuelva "El dispositivo está encendido". 
# Luego, crea una clase derivada llamada Computadora que herede de Dispositivo 
# y añada un método procesar_datos que devuelva "Procesando datos". 
# Finalmente, crea una clase derivada llamada Laptop que herede de 
# Computadora y sobrescriba el método procesar_datos para devolver 
# "Procesando datos en la laptop". 
# Crea una instancia de Laptop y muestra los resultados de los métodos.

class Dispositivo:
    def encender(self):
        return "El dispositivo está encendido"

class Computadora(Dispositivo):
    def procesar_datos(self):
        return "Procesando datos"
    

class Laptop(Computadora):
    def procesar_datos(self):
        return "Procesando datos en la laptop"

# Crear una instancia de Laptop
mi_laptop = Laptop()

# Mostrar los métodos
print(mi_laptop.encender())  # "El dispositivo está encendido"
print(mi_laptop.procesar_datos())  # "Procesando datos en la laptop"
