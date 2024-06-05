


lista = [23, 43, 12, 56, 73, 32, 81, 21, 47]

for el in lista:
    print(el, end=", ")

print(" \n ------------------- ")


for i in range(len(lista)):
    posicion = i
    actual = lista[i]

    while posicion > 0 and actual < lista[posicion - 1 ]:  # Ordenado de MENOR a MAYOR!
        lista[posicion] = lista[posicion - 1]
        posicion -= 1

    lista[posicion] = actual 

for el in lista:
    print(el, end=", ")


    