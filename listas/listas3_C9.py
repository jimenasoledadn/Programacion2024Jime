from funciones_lista import *

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

# indice = buscar_entero_lista(numeros, numero_objetivo)
# print(f"El numero buscado esta en el indice: {indice}")

# ---

print(contar_en_lista(numeros, numero_objetivo))

# -------

print(sumar_lista(numeros))

# -----

