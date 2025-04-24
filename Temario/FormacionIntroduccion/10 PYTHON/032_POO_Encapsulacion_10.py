
# Encapsulación con Métodos de Clase y Métodos Estáticos

class Producto:
    __impuesto = 0.18  # Atributo de clase privado
    
    def __init__(self, nombre, precio):
        self.__nombre = nombre  # Atributo privado
        self.__precio = precio  # Atributo privado
    
    @classmethod
    def establecer_impuesto(cls, impuesto):
        if 0 <= impuesto <= 1:
            cls.__impuesto = impuesto
        else:
            print("El impuesto debe estar entre 0 y 1")
    
    @classmethod
    def obtener_impuesto(cls):
        return cls.__impuesto
    
    def precio_final(self):
        return self.__precio * (1 + Producto.__impuesto)

# Uso
Producto.establecer_impuesto(0.20)
producto = Producto("Laptop", 1000)
print(producto.precio_final())
print(Producto.obtener_impuesto())
