

# Crea una clase Zapatilla que tenga los atributos privados 
# __color, __precio, __talla y __stock. 
# Implementa métodos getter y setter para el color, la talla y el stock. 
# El setter del color solo permite "blanco", "negro" y "rojo", y el setter 
# de la talla permite tallas entre 36 y 45. El setter del stock debe aceptar 
# solo valores positivos. 
# El precio depende del color: "blanco" (60€), "negro" (65€) y "rojo" (70€). 
# Si el color, la talla o el stock no son válidos, muestra un mensaje indicando el error. 
# Crea una instancia de Zapatilla, permite al usuario elegir el color, 
# la talla y el stock, y muestra los detalles de la zapatilla.

class Zapatilla:
    def __init__(self, color_inicial, talla_inicial, stock_inicial):
        self.__color = color_inicial
        self.__talla = talla_inicial
        self.__stock = stock_inicial
        self.__precio = self.__establecer_precio(color_inicial)

    def get_color(self):
        return self.__color

    def get_precio(self):
        return self.__precio

    def get_talla(self):
        return self.__talla

    def get_stock(self):
        return self.__stock

    def set_color(self, nuevo_color):
        if nuevo_color in ["blanco", "negro", "rojo"]:
            self.__color = nuevo_color
            self.__precio = self.__establecer_precio(nuevo_color)
        else:
            print("Color no válido. Por favor, elija entre 'blanco', 'negro' o 'rojo'.")

    def set_talla(self, nueva_talla):
        if 36 <= nueva_talla <= 45:
            self.__talla = nueva_talla
        else:
            print("Talla no válida. Por favor, elija una talla entre 36 y 45.")

    def set_stock(self, nuevo_stock):
        if nuevo_stock >= 0:
            self.__stock = nuevo_stock
        else:
            print("Stock no válido. Por favor, elija un valor positivo.")

    def __establecer_precio(self, color):
        precios = {
            "blanco": 60,
            "negro": 65,
            "rojo": 70
        }
        return precios.get(color, 0)

# Crear una instancia de Zapatilla con un color, una talla y un stock iniciales válidos
mi_zapatilla = Zapatilla("blanco", 40, 10)

# Mostrar el color, la talla, el stock y el precio iniciales
print(f"Color inicial de la zapatilla: {mi_zapatilla.get_color()}, Talla: {mi_zapatilla.get_talla()}, Stock: {mi_zapatilla.get_stock()}, Precio: {mi_zapatilla.get_precio()}€")

# Permitir al usuario elegir un nuevo color
nuevo_color = input("Elige un color para la zapatilla (blanco, negro, rojo): ").strip().lower()
mi_zapatilla.set_color(nuevo_color)

# Intentar establecer un color hasta que sea válido
while mi_zapatilla.get_color() != nuevo_color:
    nuevo_color = input("Elige un color para la zapatilla (blanco, negro, rojo): ").strip().lower()
    mi_zapatilla.set_color(nuevo_color)

# Permitir al usuario elegir una nueva talla
nueva_talla = int(input("Elige una talla para la zapatilla (36-45): ").strip())
mi_zapatilla.set_talla(nueva_talla)

# Intentar establecer una talla hasta que sea válida
while mi_zapatilla.get_talla() != nueva_talla:
    nueva_talla = int(input("Elige una talla para la zapatilla (36-45): ").strip())
    mi_zapatilla.set_talla(nueva_talla)

# Permitir al usuario elegir una nueva cantidad en stock
nuevo_stock = int(input("Elige la cantidad en stock para la zapatilla: ").strip())
mi_zapatilla.set_stock(nuevo_stock)

# Intentar establecer una cantidad en stock hasta que sea válida
while mi_zapatilla.get_stock() != nuevo_stock:
    nuevo_stock = int(input("Elige la cantidad en stock para la zapatilla: ").strip())
    mi_zapatilla.set_stock(nuevo_stock)

# Mostrar el color, la talla, el stock y el precio final de la zapatilla
print(f"Color final de la zapatilla: {mi_zapatilla.get_color()}, Talla: {mi_zapatilla.get_talla()}, Stock: {mi_zapatilla.get_stock()}, Precio: {mi_zapatilla.get_precio()}€")
