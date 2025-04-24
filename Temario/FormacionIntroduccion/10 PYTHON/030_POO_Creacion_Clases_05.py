



# Clase Básica de un Círculo

import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.radio

# Uso
circulo = Circulo(5)
print("Área:", circulo.area())
print("Perímetro:", circulo.perimetro())
