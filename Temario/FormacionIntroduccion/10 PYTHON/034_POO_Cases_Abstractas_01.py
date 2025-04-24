

# Clases abstractas

from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        import math
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        import math
        return 2 * math.pi * self.radio

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto
    
    def perimetro(self):
        return 2 * (self.ancho + self.alto)

# Uso
figuras = [Circulo(5), Rectangulo(3, 4)]

for figura in figuras:
    print(f"Área: {figura.area()}, Perímetro: {figura.perimetro()}")
