


# Crea una clase base llamada Vehiculo con un atributo marca y un método arrancar. 
# Luego, crea una clase derivada llamada Coche que herede de Vehiculo y añada 
# un atributo numero_puertas y un método abrir_puertas. 
# Crea una instancia de Coche y muestra sus atributos y métodos.

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def arrancar(self):
        return "El vehículo está arrancando"

class Coche(Vehiculo):
    def __init__(self, marca, numero_puertas):
        super().__init__(marca)
        self.numero_puertas = numero_puertas

    def abrir_puertas(self):
        return f"Abrir {self.numero_puertas} puertas"

# Crear una instancia de Coche
mi_coche = Coche("Toyota", 4)

# Mostrar atributos y métodos
print(mi_coche.marca)  # Hereda el atributo marca
print(mi_coche.arrancar())  # Hereda el método arrancar
print(mi_coche.numero_puertas)  # Atributo propio de Coche
print(mi_coche.abrir_puertas())  # Método propio de Coche

