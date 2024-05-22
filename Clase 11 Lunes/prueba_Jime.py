def cargar_lista_legajos(lista:list, cantidad:int):
    from random import randint
    LEGAJO_MIN = 20000
    LEGAJO_MAX = 30000
    while cantidad > 0:
        legajo = randint(LEGAJO_MIN, LEGAJO_MAX) # pido el legajo
        if not entero_in_lista(lista,legajo):
            lista.append(legajo)
            cantidad -= 1    

def cargar_lista_nombres(lista:list, nombres: list, cantidad:int)->None:
    for i in range(cantidad):
        lista.append(nombres[i])
        
def entero_in_lista(values:list, target:int)->bool:
    try:
        buscar_entero_lista(values, target)
        return True
    except:
        return False
        
def buscar_entero_lista(values:list, target:int)->int:
    for i in range(len(values)):
        if values[i] == target: 
            return i
    raise ValueError(f"{target} NO esta en lista")

def cargar_lista_enteros_random(lista, cant, desde, hasta):
    from random import randint
    for _ in range(cant):
        lista.append(randint(desde, hasta))
        
def cargar_lista_notas(lista, cantidad):
    cargar_lista_enteros_random(lista, cantidad, 0, 10)

def calcular_promedio(a,b)->float:
    return (a+b)/2

def cargar_lista_promedios(lista_a:list, lista_b:list, lista_proms:list)->None:
    """Recibe 3 listas, LEE las 2 primeras e indice a indice calcula el promedio y lo guarda en el mismo indice en la lista de proms 

    Args:
        lista_a (_type_): recibe una lista
        lista_b (_type_): recibe otra lista
        lista_proms (_type_): en esta lista guarda el promedio de las dos listas anteriores
    """
    tam = len(lista_a)
    for i in range(tam):
        lista_proms.append(calcular_promedio(lista_a[i], lista_b[i]))

def mostrar_alumnos(legs, names, n1, n2, proms):
    for i in range(len(legs)): # Pongo cualquier proms ya que todas van a tener la misma cantidad de elementos
        print(f"{legs[i]} {names[i]} {n1[i]} {n2[i]} {proms[i]}")
    print()

def cargar_alumnos_random(legs:list, names:list, notas_p1:list, notas_p2:list, promedios:list, cantidad:int):
    cargar_lista_legajos(legs, cantidad)
    cargar_lista_nombres(names, nombres, cantidad)
    cargar_lista_notas(notas_p1, cantidad)
    cargar_lista_notas(notas_p2, cantidad)
    cargar_lista_promedios(notas_p1, notas_p2, promedios)
    
# ----------------------------

nombres = ["Juan", "Laura", "Pedro", "Sofía", "Diego", "María", "Carlos", "Ana", "Luisa", "Javier", "Elena", "Pablo", "Isabel", "Andrés"]

legajos = []
nombres2 = []
notas_p1 = []
notas_p2 = []
promedios = []

# Aca es la llamada a la funcion. En donde me tira el error.
cargar_alumnos_random(legajos, nombres2, notas_p1, notas_p2, promedios, 10)
mostrar_alumnos(legajos, nombres2, notas_p1, notas_p2, promedios)