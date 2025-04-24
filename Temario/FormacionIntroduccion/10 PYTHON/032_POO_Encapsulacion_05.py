

# Crea una clase Estudiante con atributos privados __nombre y __nota. 
# Implementa métodos getter para ambos atributos y un método setter para __nota 
# que solo permita valores entre 0 y 10. Crea una instancia de Estudiante, 
# establece y muestra sus valores usando los métodos adecuados.

class Estudiante:
    def __init__(self, nombre, nota):
        self.__nombre = nombre
        self.__nota = nota

    def get_nombre(self):
        return self.__nombre

    def get_nota(self):
        return self.__nota

    def set_nota(self, nueva_nota):
        if 0 <= nueva_nota <= 10:
            self.__nota = nueva_nota
        else:
            print("La nota debe estar entre 0 y 10.")

# Crear una instancia de Estudiante
estudiante = Estudiante("Ana", 8)

# Mostrar el nombre y la nota
print("Nombre:", estudiante.get_nombre())
print("Nota inicial:", estudiante.get_nota())

# Intentar establecer una nueva nota válida e inválida
estudiante.set_nota(9)
print("Nueva nota válida:", estudiante.get_nota())

estudiante.set_nota(15)
print("Nota después del intento inválido:", estudiante.get_nota())
