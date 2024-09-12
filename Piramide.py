import math

# Definir la clase Piramide
class Piramide:
    def __init__(self):
        # Pedir los datos al usuario dentro del constructor
        self.lado_base = float(input("Ingresa el lado de la base de la pirámide: "))
        self.altura = float(input("Ingresa la altura de la pirámide: "))
    
    # Método para calcular el área de la base
    def area_base(self):
        return self.lado_base ** 2
    
    # Método para calcular el área lateral
    def area_lateral(self):
        apotema = math.sqrt((self.lado_base / 2) ** 2 + self.altura ** 2)
        perimetro_base = 4 * self.lado_base
        return (perimetro_base * apotema) / 2
    
    # Método para calcular el área total
    def area_total(self):
        return self.area_base() + self.area_lateral()
    
    # Método para ejecutar el cálculo y mostrar el resultado
    def mostrar_area(self):
        area = self.area_total()
        print(f"El área total de la pirámide es: {area:.2f}")

# Crear una instancia de la clase Piramide y ejecutar el cálculo
if __name__ == "__main__":
    piramide = Piramide()
    piramide.mostrar_area()