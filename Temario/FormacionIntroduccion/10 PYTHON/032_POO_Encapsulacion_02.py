
# Crea una clase CuentaBancaria que tenga un atributo privado __saldo. 
# Implementa un método getter llamado get_saldo que devuelva el saldo actual. 
# Crea una instancia de CuentaBancaria y muestra el saldo usando el método getter.

class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    def get_saldo(self):
        return self.__saldo

# Crear una instancia de CuentaBancaria
mi_cuenta = CuentaBancaria(1000)

# Mostrar el saldo usando el método getter
print("Saldo inicial:", mi_cuenta.get_saldo())
