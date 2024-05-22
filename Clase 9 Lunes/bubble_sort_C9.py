



lista = [8, 5, 4, 9, 2] # Se pregunta si 2 elementos de la lista que estoy comparando estan ordenados, si estan ordenados se dejan como estan, si estan desordenados se los invierte.

for i in range(len(lista) -1):
    for j in range(i+1, len(lista)):
        print(i,j)

    print("-----")

# Ordeno de forma Descendente:
for i in range(len(lista) - 1):
    for j in range(i+1, len(lista)):
        if lista[i] < lista[j]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

print(lista)
print("---------")

# Ordeno de forma Ascendente:
for i in range(len(lista) - 1):
    for j in range(i+1, len(lista)):
        if lista[i] > lista[j]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

print(lista)