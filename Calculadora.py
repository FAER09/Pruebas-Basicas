class Calculadora:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        # Cambio intencional para provocar fallo en las pruebas
        return a - b + 1
