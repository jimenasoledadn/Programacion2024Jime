def mostrar_lista(lista:list)->None:
    """Recorre y muestra por consola los elementos de una lista

    Args:
        lista (list): Lista a mostrar
    """
    for element in lista:
        print(element, end=" ")
    print() # para que deje el cursor en la linea de abajo

    # OTRA FORMA
        # for i in range(len(lista)):
        #     print(lista[i], end=" ")

def mayor_lista(values:list)->int: # Podemos validar que es una lista, COMO HACER ?????
    flag_mayor = True
    for i in values:
        if flag_mayor or mayor < i:
            mayor = i
            flag_mayor = False
    return mayor

# ----------------------------------------------------------

CANT = 5
lista_consola = []

for i in range(CANT): 
    numero = int(input("Ingrese un numero: "))
    lista_consola.append(numero)

mostrar_lista(lista_consola)

# ---- CLASE 9 --------
    # Obtener el mayor de esa lista de numeros:
    # UNA FORMA : --- 
# flag_mayor = True
# for i in lista_consola:
#     if flag_mayor or mayor < i:
#         mayor = i
#         flag_mayor = False
        # OTRA FORMA :
            # mayor = lista_consola[0]

            # for i in lista_consola:
            #     if i < mayor:
            #         mayor = n

mayor = mayor_lista(lista_consola)
print(f"El mayor de los numeros de esa lista es el: {mayor} ")  

