



lista = [8, 5, 4, 9, 2] # Se pregunta si 2 elementos de la lista que estoy comparando estan ordenados, si estan ordenados se dejan como estan, si estan desordenados se los invierte.

for i in range(len(lista) -1):
    for j in range(i+1, len(lista)):
        print(i,j)

    print("-----")