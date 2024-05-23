from data_warehouse_C11 import *
from funciones_paralelas_C11 import *

# quiero guardar la info de 5 alumnos:
# legajo, nota 1p, nota 2p, promedio
    
    # Ordenajr los alumnos por promedio de mejor a peor
# ---------------------------------------
TAM = 10

legajos = []
nombres = []
generos = []
notas_p1 = []
notas_p2 = []
promedios = []

        # LO COMENTAMOS PARA HARDCODEAR:
    # En cada iteracion lo que estoy haciendo es cargar en las promss paralelas, los datos de la misma persona
# for _ in range(TAM):
#     legajos.append(int(input("Ingrese legajo: ")))
#     nombres.append(input("Ingrese nombre: "))
#     notas_p1.append(int(input("Ingrese nota primer parcial: ")))
#     notas_p2.append(int(input("Ingrese nota segundo parcial: ")))
#     promedios.append(calcular_promedio(notas_p1[-1], notas_p2[-1])) # Le paso la ultima nota que agregue para que se agregue al mismo indice de la persona a la que le estoy ingresando los datos

cargar_alumnos_random(legajos, nombres, generos, notas_p1, notas_p2, promedios, TAM)

mostrar_alumnos(legajos, nombres, generos, notas_p1, notas_p2, promedios)

ordenar_alumnos(legajos, nombres, generos, notas_p1, notas_p2, promedios)

mostrar_alumnos(legajos, nombres, generos, notas_p1, notas_p2, promedios)