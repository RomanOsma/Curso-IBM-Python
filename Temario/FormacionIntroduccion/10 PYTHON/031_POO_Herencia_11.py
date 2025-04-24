





# Crea una clase base llamada Animal con un atributo nombre y un método hacer_sonido. 
# Luego, crea una clase derivada llamada Perro que herede de Animal y añada 
# un atributo raza y un método ladrar. Crea una instancia de Perro y muestra sus atributos y métodos.

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return "Algún sonido genérico"

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def ladrar(self):
        return "Guau guau"

# Crear una instancia de Perro
mi_perro = Perro("Rex", "Labrador")

# Mostrar atributos y métodos
print(mi_perro.nombre)  # Hereda el atributo nombre
print(mi_perro.hacer_sonido())  # Hereda el método hacer_sonido
print(mi_perro.raza)  # Atributo propio de Perro
print(mi_perro.ladrar())  # Método propio de Perro