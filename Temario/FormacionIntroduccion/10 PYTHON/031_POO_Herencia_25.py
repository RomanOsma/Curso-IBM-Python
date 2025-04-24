
# Herencia Múltiple Básica

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def detalles(self):
        return f"Vehiculo: {self.marca}"
    

class Motor:
    def __init__(self, tipo_motor):
        self.tipo_motor = tipo_motor

    def detalles(self):
        return f"Motor: {self.tipo_motor}"    

class Coche(Motor, Vehiculo):
    def __init__(self, marca, tipo_motor, modelo):
        Vehiculo.__init__(self, marca)
        Motor.__init__(self, tipo_motor)
        self.modelo = modelo
    
    def descripcion(self):
        return f"{self.marca} {self.modelo} con motor {self.tipo_motor}"


# Uso
coche = Coche("Toyota", "V6", "Corolla")
print(coche.descripcion())
print(coche.detalles())
