
# Constructores en herencia

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)  # Llama al constructor de la clase base
        self.raza = raza

    def hacer_sonido(self):
        return "Guau"

# Crear una instancia de la clase Perro
perro = Perro("Firulais", "Labrador")
print(f"{perro.nombre} es un {perro.raza} y dice {perro.hacer_sonido()}")  # Salida: Firulais es un Labrador y dice Guau

