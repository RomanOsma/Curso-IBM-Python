
# Crea una clase Zapatilla que tenga un atributo privado __color. 
# Implementa métodos getter y setter para el color, donde el setter 
# solo permita los colores "blanco", "negro" y "rojo". 
# Si se intenta establecer un color no válido, muestra un mensaje 
# indicando que el color no es válido y pide al usuario que elija 
# un color válido. 
# Crea una instancia de Zapatilla, permite al usuario elegir un color 
# y muestra el color de la zapatilla.


class Zapatilla:
    def __init__(self, color_inicial):
        self.__color = color_inicial

    def get_color(self):
        return self.__color

    def set_color(self, nuevo_color):
        if nuevo_color in ["blanco", "negro", "rojo"]:
            self.__color = nuevo_color
        else:
            print("Color no válido. Por favor, elija entre 'blanco', 'negro' o 'rojo'.")

# Crear una instancia de Zapatilla con un color inicial válido
mi_zapatilla = Zapatilla("blanco")

# Mostrar el color inicial
print("Color inicial de la zapatilla:", mi_zapatilla.get_color())

# Permitir al usuario elegir un nuevo color
nuevo_color = input("Elige un color para la zapatilla (blanco, negro, rojo): ").strip().lower()
mi_zapatilla.set_color(nuevo_color)

# Intentar establecer un color hasta que sea válido
while mi_zapatilla.get_color() != nuevo_color:
    nuevo_color = input("Elige un color para la zapatilla (blanco, negro, rojo): ").strip().lower()
    mi_zapatilla.set_color(nuevo_color)

# Mostrar el color final de la zapatilla
print("Color final de la zapatilla:", mi_zapatilla.get_color())
