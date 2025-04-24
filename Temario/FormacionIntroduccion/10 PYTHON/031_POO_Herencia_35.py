

# Herencia Múltiple con Propiedades y Métodos Especiales

class Nadador:
    def nadar(self):
        return "Estoy nadando"

class Corredor:
    def correr(self):
        return "Estoy corriendo"

class Triatleta(Nadador, Corredor):
    def __init__(self, nombre):
        self.nombre = nombre

    def competir(self):
        return f"{self.nombre} compite en triatlón: {self.nadar()}, {self.correr()}."

# Uso
triatleta = Triatleta("Laura Sánchez")
print(triatleta.competir())
