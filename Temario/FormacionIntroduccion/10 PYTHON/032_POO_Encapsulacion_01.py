
# Encapsulación Básica con Atributos Privados

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad      # Atributo privado
    
    def obtener_nombre(self):
        return self.__nombre
    
    def establecer_nombre(self, nombre):
        self.__nombre = nombre
    
    def obtener_edad(self):
        return self.__edad
    
    def establecer_edad(self, edad):
        if edad > 0:
            self.__edad = edad
        else:
            print("La edad debe ser positiva")

# Uso
persona = Persona("Juan", 30)
print(persona.obtener_nombre())
persona.establecer_edad(35)
print(persona.obtener_edad())
print(persona.edad)
