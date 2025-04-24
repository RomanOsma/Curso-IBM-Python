
# Constructores

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Inicializa el atributo nombre
        self.edad = edad      # Inicializa el atributo edad

    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

# Crear una instancia de la clase Persona
persona = Persona("Ana", 30)
print(persona.presentarse())  # Salida: Hola, soy Ana y tengo 30 años.
