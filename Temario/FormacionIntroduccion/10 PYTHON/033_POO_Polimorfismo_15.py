
# Polimorfismo con Interfaces Implícitas

class Pato:
    def hacer_sonido(self):
        return "Cuac"

class Persona:
    def hacer_sonido(self):
        return "Hola"

def llamar_sonido(cosa):
    print(cosa.hacer_sonido())

# Uso
pato = Pato()
persona = Persona()

llamar_sonido(pato)    # Salida: Cuac
llamar_sonido(persona) # Salida: Hola
