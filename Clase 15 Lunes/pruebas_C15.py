


def reduce_lista(funcion, lista:list):
    ant = lista[0]
    for i in range(1, len(lista)):
        ant = funcion(ant, lista[i])
    return ant

# -----------------------

x = [4,3,6,5,7,5,7,45,78,2]
y = sum(x)

suma = reduce_lista(lambda ant, act: ant + act, x)
mayor = reduce_lista(lambda ant, act: ant if ant > act else act, x)
y = max(x)

print(mayor)
print(y)

