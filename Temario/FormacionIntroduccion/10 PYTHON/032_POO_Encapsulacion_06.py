

# Crea una clase Libro con un atributo privado __titulo y un método 
# privado __mostrar_titulo que imprime el título del libro. 
# Implementa un método público leer_titulo que llame al método 
# privado __mostrar_titulo. 
# Crea una instancia de Libro y llama al método leer_titulo.

class Libro:
    def __init__(self, titulo):
        self.__titulo = titulo

    def __mostrar_titulo(self):
        print(f"El título del libro es: {self.__titulo}")

    def leer_titulo(self):
        self.__mostrar_titulo()

# Crear una instancia de Libro
mi_libro = Libro("El Principito")

# Llamar al método leer_titulo
mi_libro.leer_titulo()
