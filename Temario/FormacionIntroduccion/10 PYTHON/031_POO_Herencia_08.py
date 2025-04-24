

# Crea una clase base llamada SerVivo con un método respirar que 
# devuelva "Estoy respirando". 
# Luego, crea una clase derivada llamada Animal que herede de SerVivo 
# y añada un método moverse que devuelva "Me estoy moviendo". 
# Finalmente, crea una clase derivada llamada Perro que herede 
# de Animal y sobrescriba el método moverse para devolver "Estoy corriendo". 
# Crea una instancia de Perro y muestra los resultados de los métodos.


class SerVivo:
    def respirar(self):
        return "Estoy respirando"

class Animal(SerVivo):
    def moverse(self):
        return "Me estoy moviendo"

class Perro(Animal):
    def moverse(self):
        return "Estoy corriendo"

# Crear una instancia de Perro
mi_perro = Perro()

# Mostrar los métodos
print(mi_perro.respirar())  # "Estoy respirando"
print(mi_perro.moverse())  # "Estoy corriendo"
