

def cargar_lista_enteros_random(lista, cant, desde, hasta):
    from random import randint
    for _ in range(cant):
        lista.append(randint(desde, hasta)) # la funcion randint  

def crear_lista_enteros_random(cant, desde, hasta)->list:
    values = []
    from random import randint
    for _ in range(cant):
        values.append(randint(desde, hasta)) 
    return values
# REUTILIZACION DE CODIGO:
    # def crear_lista_enteros_random(cant, desde, hasta)->list:
    #     values = []
    #     cargar_lista_enteros_random(values, cant, desde, hasta)
    #     return values      

def mostrar_lista(lista:list)->None:
    """Recorre y muestra por consola los elementos de una lista

    Args:
        lista (list): Lista a mostrar
    """
    for element in lista:
        print(element, end=" ")
    print()

def mayor_lista(values:list)->int: # Podemos validar que es una lista, COMO HACER ?????
    flag_mayor = True
    for i in values:
        if flag_mayor or mayor < i:
            mayor = i
            flag_mayor = False
    return mayor

def entero_in_lista(values:list, target:int)->bool:
    esta = False
    for value in values:
        if value == target:
            esta = True
            break
    return esta

    # Me tiene que devolver el indice en el que esta la primera vez, y si NO esta -1
def buscar_entero_lista(values:list, target:int)->int:
    indice_target = -1
    for i in range(len(values)): # xq quiero ver cada posicion en la lista
        if values[i] == target:
            indice_target = i
            break
    return indice_target



# ---------------
CANT = 20
MIN = 1
MAX = 100

    # numeros = []

    # cargar_lista_enteros_random(numeros, 20, 1, 100)

numeros = crear_lista_enteros_random(CANT, MIN, MAX)
mostrar_lista(numeros)

# Mostrar el mayor:
print("El mayor de la lista es el:", mayor_lista(numeros))

# ---------------------------

    # TAREA: decir si el numero objetivo esta en la lista:

numero_objetivo = 20

if entero_in_lista(numeros, numero_objetivo): # Si esto es verdadero:
    print(f"El numero objetivo {numero_objetivo} esta en la lista")
else:
    print(f"El numero objetivo {numero_objetivo} NO esta en la lista")

# -------------------------------

indice = buscar_entero_lista(numeros, numero_objetivo)
print(indice)

