

# Constuctores con valores por defecto

class Persona:
    def __init__(self, nombre="Desconocido", edad=0):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

# Crear instancias de la clase Persona con y sin valores por defecto
persona1 = Persona()
persona2 = Persona("Ana", 30)

print(persona1.presentarse())  # Salida: Hola, soy Desconocido y tengo 0 años.
print(persona2.presentarse())  # Salida: Hola, soy Ana y tengo 30 años.
