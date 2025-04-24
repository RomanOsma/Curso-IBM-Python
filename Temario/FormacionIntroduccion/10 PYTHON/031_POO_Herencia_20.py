

# Herencia con Métodos Adicionales y Atributos (Empleado y Programador)

class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
    
    def detalles(self):
        return f"Empleado: {self.nombre}, Edad: {self.edad}, Salario: ${self.salario}"

class Programador(Empleado):
    def __init__(self, nombre, edad, salario, lenguajes):
        super().__init__(nombre, edad, salario)
        self.lenguajes = lenguajes
    
    def detalles(self):
        return f"Programador: {self.nombre}, Edad: {self.edad}, Salario: ${self.salario}, Lenguajes: {', '.join(self.lenguajes)}"
    
    def agregar_lenguaje(self, lenguaje):
        self.lenguajes.append(lenguaje)

# Uso
empleado = Empleado("Juan Pérez", 30, 50000)
programador = Programador("Ana Gómez", 25, 60000, ["Python", "JavaScript"])
print(empleado.detalles())
print(programador.detalles())

programador.agregar_lenguaje("Java")
print(programador.detalles())
