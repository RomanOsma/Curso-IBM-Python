


# Clase para una Calculadora Simple

class Calculadora:
    def __init__(self):
        self.resultado = 0
    
    def sumar(self, valor):
        self.resultado += valor
        return self.resultado
    
    def restar(self, valor):
        self.resultado -= valor
        return self.resultado
    
    def multiplicar(self, valor):
        self.resultado *= valor
        return self.resultado
    
    def dividir(self, valor):
        if valor != 0:
            self.resultado /= valor
        else:
            print("Error: División por cero")
        return self.resultado

# Uso
calc = Calculadora()
print("Suma:", calc.sumar(5))
print("Resta:", calc.restar(2))
print("Multiplicación:", calc.multiplicar(3))
print("División:", calc.dividir(4))
