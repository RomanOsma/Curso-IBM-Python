
# Crea una clase Empleado que tenga un atributo protegido _sueldo y un método 
# público mostrar_sueldo que imprima el sueldo. Crea una instancia de Empleado 
# y llama al método mostrar_sueldo.

class Empleado:
    def __init__(self, sueldo_inicial):
        self._sueldo = sueldo_inicial

    def mostrar_sueldo(self):
        print(f"El sueldo es: {self._sueldo}")

# Crear una instancia de Empleado
empleado = Empleado(50000)

# Llamar al método mostrar_sueldo
empleado.mostrar_sueldo()
