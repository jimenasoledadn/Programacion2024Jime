



def  duplicar_valores(lista):
    for i in range(len(lista)):
        lista[i] = lista[i] * 2

# ---------

l = [3, 6, 8, 15, 90]

print(l)
duplicar_valores(l)

print(l)