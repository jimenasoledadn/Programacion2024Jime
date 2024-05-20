# quiero guardar la info de 5 alumnos:
# legajo, nota 1p, nota 2p, promedio

def promediar_notas(n1, n2):
    return (n1 + n2) / 2

def mostrar_alumnos(legs, names, n1, n2, proms):
    for i in range(len(legs)): # Pongo cualquier lista ya que todas van a tener la misma cantidad de elementos
        print(f"{legs[i]} {names[i]} {n1[i]} {n2[i]} {proms[i]}")
    print()

def ordenar_alumnos():
    pass
    # Ordenajr los alumnos por promedio de mejor a peor
# ---------------------------------------

TAM = 3

legajos = []
nombres = []
notas_p1 = []
notas_p2 = []
promedios = []

    # En cada iteracion lo que estoy haciendo es cargar en las listas paralelas, los datos de la misma persona
for _ in range(TAM):
    legajos.append(int(input("Ingrese legajo: ")))
    nombres.append(input("Ingrese nombre: "))
    notas_p1.append(int(input("Ingrese nota primer parcial: ")))
    notas_p2.append(int(input("Ingrese nota segundo parcial: ")))
    promedios.append(promediar_notas(notas_p1[-1], notas_p2[-1])) # Le paso la ultima nota que agregue para que se agregue al mismo indice de la persona a la que le estoy ingresando los datos


mostrar_alumnos(legajos, nombres, notas_p1, notas_p2, promedios)


