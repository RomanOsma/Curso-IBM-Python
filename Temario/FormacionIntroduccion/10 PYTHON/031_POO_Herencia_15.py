

# Herencia con Métodos Sobrescritos (Vehículo, Coche, y Bicicleta)

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def descripcion(self):
        return f"{self.marca} {self.modelo}"
    
    def tipo(self):
        pass

class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas
    
    def tipo(self):
        return "Coche"

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo_bicicleta):
        super().__init__(marca, modelo)
        self.tipo_bicicleta = tipo_bicicleta
    
    def tipo(self):
        return "Bicicleta"

# Uso
coche = Coche("Toyota", "Corolla", 4)
bicicleta = Bicicleta("Giant", "Escape 3", "Híbrida")
print(coche.descripcion(), "-", coche.tipo())
print(bicicleta.descripcion(), "-", bicicleta.tipo())

