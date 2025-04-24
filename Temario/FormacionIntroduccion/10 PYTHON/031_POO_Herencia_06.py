

# Herencia básica

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def arrancar(self):
        return "El vehículo está arrancando"

class Coche(Vehiculo):
    pass

# Uso
mi_coche = Coche("Toyota")
print(mi_coche.marca)  # Hereda el atributo marca
print(mi_coche.arrancar())  # Hereda el método arrancar
