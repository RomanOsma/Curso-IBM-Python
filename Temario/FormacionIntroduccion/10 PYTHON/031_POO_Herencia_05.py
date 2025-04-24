

# Herencia Básica (Animal y Perro)

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"



# Uso
perro = Perro("Firulais")
print(perro.nombre)
print(perro.hacer_sonido())
