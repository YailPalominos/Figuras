import math
#Clase para calcular el área de un pentagono
#Luis Gerardo Suárez Pérez.

def calcular_area_pentagono():
    while True:
        try:
            lado = float(input("Ingrese la longitud de un lado del pentágono: "))
            if lado <= 0:
                print("La longitud del lado debe ser un número positivo. Intente de nuevo.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

    # Fórmula del área de un pentágono regular: (5 * lado^2) / (4 * tan(π/5))
    area = (5 * lado ** 2) / (4 * math.tan(math.pi / 5))
    
    print(f"El área del pentágono es: {area:.2f} unidades")

# Llamada a la función
calcular_area_pentagono()
