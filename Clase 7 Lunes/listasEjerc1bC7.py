def mostrar_lista(lista:list)->None:
    """Recorre y muestra por consola los elementos de una lista

    Args:
        lista (list): Lista a mostrar
    """
    for i in range(len(lista)):
        print(lista[i], end=" ")
    # OTRA FORMA
    # for element in lista:
    #     print(element, end=" ")
    # print()

CANT = 5
lista_consola = []

for i in range(CANT): 
    numero = int(input("Ingrese un numero: "))
    lista_consola.append(numero)

mostrar_lista(lista_consola)

