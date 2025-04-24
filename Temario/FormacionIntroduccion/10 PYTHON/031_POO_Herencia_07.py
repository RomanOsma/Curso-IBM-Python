


# Herencia básica

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

class Estudiante(Persona):
    pass

class Profesor(Persona):
    
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} , tengo {self.edad} años y soy profesor de matemáticas"

# Uso
estudiante = Estudiante("Ana", 21)
print(estudiante.nombre)  # Hereda el atributo nombre
print(estudiante.edad)  # Hereda el atributo edad
print(estudiante.saludar())  # Hereda el método saludar

profMate = Profesor("D. Miguel", 54)
print(profMate.nombre)
print(profMate.saludar())


