

# Polimorfismo con Métodos

class Perro:
    def hacer_sonido(self):
        return "Guau"

class Gato:
    def hacer_sonido(self):
        return "Miau"

def hacer_sonidos(animal):
    print(animal.hacer_sonido())

# Uso
perro = Perro()
gato = Gato()

hacer_sonidos(perro)  # Salida: Guau
hacer_sonidos(gato)   # Salida: Miau
