
# Modifica la clase CuentaBancaria para que tenga un método setter llamado set_saldo 
# que permita modificar el saldo solo si el nuevo saldo es positivo. 
# Usa este método para intentar establecer un saldo negativo y observa el resultado.

class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self.__saldo = nuevo_saldo
        else:
            print("El saldo no puede ser negativo.")

# Crear una instancia de CuentaBancaria
mi_cuenta = CuentaBancaria(1000)

# Intentar establecer un saldo negativo
mi_cuenta.set_saldo(-500)

# Mostrar el saldo después del intento
print("Saldo después del intento:", mi_cuenta.get_saldo())
