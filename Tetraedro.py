#Kevin Jesús Martin López Doblado
#Función matemática
import math 
#Método que calcula la superficie de un tetraedro con el valor de la arista
def areaTetraedo(arista):
    #Formula para el calculo
    resultado = math.sqrt(3)*(arista ** 2) 
    return resultado
#Variable para capturar la longitud de la arista del tetraedro
longitudArista =float(input("Ingrese la longitud de la arista: "))
#Llamada a la función areaTetraedro
uts = areaTetraedo(longitudArista)

#Imprime el área de la superficie del Tetraedro
print(f"El área de la superficie del tetraedro es: {uts}")
input("Presiona Enter para salir")
