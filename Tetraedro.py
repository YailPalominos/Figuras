import math

def areaTetraedo(arista):
    resultado = math.sqrt(3)*(arista ** 2) 
    return resultado

longitudArista =float(input("Ingrese la longitud de la arista: "))
uts = areaTetraedo(longitudArista)

print(f"El área de la superficie del tetraedro es: {uts}")
input("Presiona Enter para salir")
