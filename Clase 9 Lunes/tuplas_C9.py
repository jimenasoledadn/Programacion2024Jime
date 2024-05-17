



        # lista = [2, 4, 5, 7, 10]
        # tupla = (2, 4, 5, 7, 10)

        # print(lista)
        # print(type(lista))
        # print(tupla)
        # print(type(tupla))

# -- Si quisiera recorrer una lista la puedo convertir en Tupla:

lista = [2, 4, 5, 7, 10]
print(lista)
tupla = tuple(lista)
print(tupla)
# reconvertirla:
lista2 = list(tupla)
print(lista2)
print("-----")

# --- DESESTRUCTURACION de Tuplas:

tupla = (4, 5)
x , y = tupla
print(x)
print(y)
print("-----")

# --- INVERTIR los elementos de una tupla:

tupla = (4, 5)
print(tupla)
x , y = tupla
tupla = ( y , x )
print(tupla)
print("-----")