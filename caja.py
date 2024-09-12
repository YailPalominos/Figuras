import math 

class Caja:
    def __init__(self):
        # Pedir las dimensiones de la caja
        self.base = float(input("Cuánto mide la base de la caja: "))
        self.altura = float(input("Cuánto mide la altura de la caja: "))
        self.ancho = float(input("Cuánto mide el ancho de la caja: "))

    # Método para calcular el área total
    def area_total(self):
        return 2 * (self.base * self.altura + self.base * self.ancho + self.altura * self.ancho)

    # Método para mostrar el área
    def mostrar_area(self):
        area = self.area_total()
        print(f"El área total de la caja es: {area:.2f} unidades cuadradas")

# Ejecutar el programa
if __name__ == "__main__":
    cubo = Caja()
    cubo.mostrar_area()
