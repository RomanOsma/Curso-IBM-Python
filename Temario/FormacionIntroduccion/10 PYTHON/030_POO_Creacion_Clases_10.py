
# Clase para un Libro

class Libro:

    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
    
    def descripcion(self):
        return f"'{self.titulo}' por {self.autor} ({self.anio_publicacion})"
    
    # def is_antiguo(self):
    #     return self.anio_publicacion < 1968

# Uso
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967)
libro2 = Libro("El quijote", "M.Cervantes", "Mil seiscientos cinco")

print(libro1.descripcion())
print(libro1.titulo)
print(libro2.descripcion())

# print("¿Es antiguo?", libro1.is_antiguo())
# print("¿Es antiguo?", libro2.is_antiguo())