

# Encapsulación con Métodos y Propiedades

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular  # Atributo privado
        self.__saldo = saldo      # Atributo privado
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, monto):
        if monto >= 0:
            self.__saldo = monto
        else:
            print("El saldo no puede ser negativo")
    
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
        else:
            print("El monto a depositar debe ser positivo")
    
    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
        else:
            print("Monto inválido o saldo insuficiente")

# Uso
cuenta = CuentaBancaria("Ana", 1000)
cuenta.depositar(500)
print(cuenta.saldo)
cuenta.retirar(200)
print(cuenta.saldo)
cuenta.saldo = 1500  # Usando el setter
print(cuenta.saldo)
print(cuenta._CuentaBancaria__saldo) # Accediendo a una propiedad privada. NO RECOMENDADO!!!!
