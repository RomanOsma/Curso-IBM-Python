


# Crea una clase base llamada Persona con atributos nombre y edad, y un método saludar. 
# Luego, crea una clase derivada llamada Estudiante que herede de Persona y 
# añada un atributo carrera y un método estudiar. 
# Crea una instancia de Estudiante y muestra sus atributos y métodos.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def estudiar(self):
        return f"Estoy estudiando {self.carrera}."

# Crear una instancia de Estudiante
estudiante = Estudiante("Ana", 21, "Ingeniería")

# Mostrar atributos y métodos
print(estudiante.nombre)  # Hereda el atributo nombre
print(estudiante.edad)  # Hereda el atributo edad
print(estudiante.saludar())  # Hereda el método saludar
print(estudiante.carrera)  # Atributo propio de Estudiante
print(estudiante.estudiar())  # Método propio de Estudiante
