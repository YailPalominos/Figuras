#Clase para calcular la superficie de un cilindro
import math

class Cilindro:
    def __init__(self):
        self.radio = float(input("Ingresa el radio del cilindro"))
        self.altura = float(input("Ingresa la altura del cilindro"))

    # Método para calcular el área lateral del cilindro
    def area_lateral(self):
        return 2 * math.pi * self.radio * self.altura

    # Método para calcular el área de las dos bases del cilindro
    def area_bases(self):
        return 2 * math.pi * (self.radio ** 2)

    # Método para calcular el área total de la superficie del cilindro
    def area_total(self):
        return self.area_lateral() + self.area_bases()

# Ejemplo de uso
if __name__ == "__main__":
    cilindro = Cilindro()

    print(f"Área lateral del cilindro: {cilindro.area_lateral():.2f}")
    print(f"Área de las bases del cilindro: {cilindro.area_bases():.2f}")
    print(f"Área total del cilindro: {cilindro.area_total():.2f}")