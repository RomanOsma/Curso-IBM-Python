def decorador(funcion):
    def envoltura():
        print("Antes de ejecutar la función")
        funcion()  # Llamada a la función original
        print("Después de ejecutar la función")
    return envoltura

@decorador
def saludo():
    print("Hola, mundo!")

saludo()




