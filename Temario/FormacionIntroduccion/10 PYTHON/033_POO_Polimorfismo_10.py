
# Polimorfismo con Herencia y Métodos Sobrescritos

class Figura:
    def area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        import math
        return math.pi * self.radio ** 2

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto

# Uso
figuras = [Circulo(5), Rectangulo(3, 4)]

for figura in figuras:
    print(f"Área: {figura.area()}")
