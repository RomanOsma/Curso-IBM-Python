



# Crea una jerarquía de clases para un sistema de trabajo en una empresa. 
# Comienza con una clase base Persona (abuelo), luego crea una clase 
# derivada Empleado (padre) que herede de Persona, y finalmente, una 
# clase Gerente (hija) que herede de Empleado. 
# Además, añade una clase Habilidad que represente habilidades adicionales 
# que un empleado puede tener. 
# Haz que Gerente herede tanto de Empleado como de Habilidad (herencia múltiple).

# Asegúrate de:

# Utilizar atributos y métodos en cada clase.
# Sobrescribir métodos en las clases derivadas.
# Utilizar super() para llamar a métodos de las clases base.
# Mostrar el uso de la herencia múltiple.


# Clase base
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."

# Clase derivada de Persona
class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)  # Llamada a constructor de Persona
        self.salario = salario

    def presentarse(self):
        # Sobrescribir método presentarse y usar super()
        return super().presentarse() + f" Soy empleado y gano {self.salario} euros al año."

    def trabajar(self):
        return "Estoy trabajando."

# Otra clase base para herencia múltiple
class Habilidad:
    def __init__(self, habilidades):
        self.habilidades = habilidades

    def mostrar_habilidades(self):
        return f"Tengo las siguientes habilidades: {', '.join(self.habilidades)}"

# Clase derivada de Empleado y Habilidad (herencia múltiple)
class Gerente(Empleado, Habilidad):
    def __init__(self, nombre, edad, salario, habilidades, departamento):
        Empleado.__init__(self, nombre, edad, salario)  # Llamada a constructor de Empleado
        Habilidad.__init__(self, habilidades)  # Llamada a constructor de Habilidad
        self.departamento = departamento

    def presentarse(self):
        # Sobrescribir método presentarse y usar super() para Empleado y Persona
        return super().presentarse() + f" Soy gerente del departamento de {self.departamento}."

    def trabajar(self):
        # Sobrescribir método trabajar
        return "Estoy supervisando a los empleados."

# Crear instancias y mostrar el uso de los métodos
persona = Persona("Juan", 50)
empleado = Empleado("Ana", 30, 35000)
gerente = Gerente("Carlos", 40, 60000, ["Liderazgo", "Gestión de proyectos"], "IT")

# Mostrar presentaciones
print(persona.presentarse())
print(empleado.presentarse())
print(gerente.presentarse())

# Mostrar trabajo
print(empleado.trabajar())
print(gerente.trabajar())

# Mostrar habilidades del gerente
print(gerente.mostrar_habilidades())
