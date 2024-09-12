# Definir la clase Cubo
class Cubo:
    def _init_(self):
        # Pedir la medida del lado del cubo dentro del constructor
        self.lado = float(input("Ingresa la longitud del lado del cubo: "))
    
    # Método para calcular el área de una cara del cubo
    def area_(self):
        return self.lado ** 2
    
    # Método para calcular el área total (6 caras)
    def area_total(self):
        return 6 * self.area_()
    
    # Método para ejecutar el cálculo y mostrar el resultado
    def mostrar_area(self):
        area = self.area_total()
        print(f"El área superficial total del cubo es: {area:.2f}")

# Crear una instancia de la clase Cubo y ejecutar el cálculo
if _name_ == "_main_":
    cubo = Cubo()
    cubo.mostrar_area()