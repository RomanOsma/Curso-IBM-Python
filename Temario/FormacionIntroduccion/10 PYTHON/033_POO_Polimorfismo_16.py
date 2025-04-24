class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_detalle(self):
        return f"Empleado: {self.nombre}, Salario: {self.salario}€"

class Director(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)  # Hereda los atributos de Empleado
        self.departamento = departamento

    def mostrar_detalle(self):
        return f"Director: {self.nombre}, Salario: {self.salario}€, Departamento: {self.departamento}"


# Función polimórfica
def imprimir_detalle(persona):
    print(persona.mostrar_detalle())


# Crear instancias de Empleado y Director
empleado = Empleado("Luis", 2500)
director = Director("Ana", 5000, "Finanzas")

# Usar la función polimórfica
imprimir_detalle(empleado)  # Llama a mostrar_detalle() de Empleado
imprimir_detalle(director)  # Llama a mostrar_detalle() de Director

