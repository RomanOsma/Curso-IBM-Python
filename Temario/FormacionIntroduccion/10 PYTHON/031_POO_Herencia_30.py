

# Herencia Múltiple con Métodos de Diferentes Clases

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Soy {self.nombre} y tengo {self.edad} años."

class Empleado:
    def __init__(self, salario):
        self.salario = salario

    def mostrar_salario(self):
        return f"Mi salario es ${self.salario}"

class Gerente(Persona, Empleado):
    def __init__(self, nombre, edad, salario, departamento):
        Persona.__init__(self, nombre, edad)
        Empleado.__init__(self, salario)
        self.departamento = departamento
    
    def detalles(self):
        return f"{self.presentarse()}, trabajo en el departamento de {self.departamento} y {self.mostrar_salario()}."

# Uso
gerente = Gerente("Carlos Martínez", 40, 75000, "Ventas")
print(gerente.detalles())
