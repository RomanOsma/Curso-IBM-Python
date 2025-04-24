

# Clase con Propiedades

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    @property
    def area(self):
        return self.ancho * self.alto
    
    @property
    def perimetro(self):
        return 2 * (self.ancho + self.alto)

# Uso
rectangulo = Rectangulo(3, 4)
print("Área:", rectangulo.area)
print("Perímetro:", rectangulo.perimetro)
