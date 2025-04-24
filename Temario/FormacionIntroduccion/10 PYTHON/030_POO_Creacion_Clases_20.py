


# Clase para una Cuenta Bancaria

class CuentaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, monto):
        self.saldo += monto
        return self.saldo
    
    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            print("Saldo insuficiente")
        return self.saldo
    
    def mostrar_saldo(self):
        return f"Saldo actual: ${self.saldo:.2f}"

# Uso
cuenta = CuentaBancaria("Juan Pérez", 1000)
print(cuenta.mostrar_saldo())
cuenta.depositar(500)
print(cuenta.mostrar_saldo())
cuenta.retirar(300)
print(cuenta.mostrar_saldo())
