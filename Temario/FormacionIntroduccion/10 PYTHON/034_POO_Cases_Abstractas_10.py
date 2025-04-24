
# Clase Abstracta con Métodos y Propiedades Abstractas

from abc import ABC, abstractmethod

class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass
    
    @property
    @abstractmethod
    def tipo(self):
        pass

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, salario_mensual):
        self.salario_mensual = salario_mensual
    
    def calcular_salario(self):
        return self.salario_mensual
    
    @property
    def tipo(self):
        return "Tiempo Completo"

class EmpleadoPorHora(Empleado):
    def __init__(self, horas_trabajadas, tarifa_por_hora):
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora
    
    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_por_hora
    
    @property
    def tipo(self):
        return "Por Hora"

# Uso
empleados = [EmpleadoTiempoCompleto(3000), EmpleadoPorHora(120, 15)]

for empleado in empleados:
    print(f"Tipo: {empleado.tipo}, Salario: {empleado.calcular_salario()}")
