# challenge --->  Formas geométricas: Define una clase base FormaGeometrica con métodos calcular_area y calcular_perimetro. Crea clases derivadas Rectangulo y Circulo que sobrescriban estos métodos.
import math

# Clase base FormaGeometrica
class FormaGeometrica:
    def calcular_area(self):
        raise NotImplementedError("Este método debe ser sobrescrito por la clase derivada")

    def calcular_perimetro(self):
        raise NotImplementedError("Este método debe ser sobrescrito por la clase derivada")

# Clase derivada Rectangulo
class Rectangulo(FormaGeometrica):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)

# Clase derivada Circulo
class Circulo(FormaGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

# Ejemplo de uso:
rectangulo = Rectangulo(4, 5)
circulo = Circulo(3)

print(f"Rectángulo - Área: {rectangulo.calcular_area()}, Perímetro: {rectangulo.calcular_perimetro()}")
print(f"Círculo - Área: {circulo.calcular_area()}, Perímetro: {circulo.calcular_perimetro()}")
