
def sort_list(lista:list, comparador)->None:
    tam = len(lista)
    for i in range(tam - 1 ):
        for j in range(i+1, tam):
            if comparador(lista[i], lista[j]) > 0:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                

def compare_persona(p1, p2):
    if p1["nombre"] == p2["nombre"]:
        return 0
    elif p1["nombre"] < p2["nombre"]:
        return -1
    else:
        return 1