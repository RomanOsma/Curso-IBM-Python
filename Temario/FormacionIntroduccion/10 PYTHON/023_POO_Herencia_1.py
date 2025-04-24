# Definición de la clase padre

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


# Definición de la clase hija que hereda de la clase padre.
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad) #Nos permite acceder a los métodos del padre
        self.sueldo = sueldo


Pepe = Persona("Pepe", 43)
print(f'La edad de Pepe es de {Pepe.edad}')

# Instancia de la clase hija.
empleado1 = Empleado('Juan', 28, 5000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)
