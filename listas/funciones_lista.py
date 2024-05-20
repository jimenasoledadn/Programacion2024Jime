

def cargar_lista_enteros_random(lista, cant, desde, hasta):
    from random import randint
    for _ in range(cant):
        lista.append(randint(desde, hasta)) # la funcion randint  

def crear_lista_enteros_random(cant, desde, hasta)->list:
    values = []
    from random import randint
    for _ in range(cant):
        values.append(randint(desde, hasta)) 
    return values
    # REUTILIZACION DE CODIGO:
        # def crear_lista_enteros_random(cant, desde, hasta)->list:
        #     values = []
        #     cargar_lista_enteros_random(values, cant, desde, hasta)
        #     return values      

def mostrar_lista(lista:list)->None:
    """Recorre y muestra por consola los elementos de una lista

    Args:
        lista (list): Lista a mostrar
    """
    #   UNA FORMA:
    if not isinstance(lista, list): # Primero la validacion
        raise TypeError("Esto no es una lista") # NO haria falta un else, ya que el RAISE es como un break, una vez que se ejecuta se sale de la funcion. Es decir es la ultima linea que se va a ejecutar en esta funcion, todo lo que este despues NUNCA se va a ejecutar, en cambio si no entra en este if, va a pasar directamente al codigo de la funcion
    
    for element in lista: # Aca queda el codigo de la funcion limpio
        print(element, end=" ")
    print()

    #   OTRA FORMA:
    # if isinstance(lista, list):
    #     for element in lista:
    #         print(element, end=" ")
    #     print()
    # else:
    #     raise TypeError("Eso no es una lista") # Esto va a mostrar por terminal que tipo de error es, y CUAL fue el error !!! 

def mayor_lista(values:list)->int: # Podemos validar que es una lista, COMO HACER ?????
    flag_mayor = True
    for i in values:
        if flag_mayor or mayor < i:
            mayor = i
            flag_mayor = False
    return mayor

def entero_in_lista(values:list, target:int)->bool:
    try:
        buscar_entero_lista(values, target)
        return True
    except: # Si NO voy a hacer uso de la excepcion SOLO dejo except solo
        return False

    # Me tiene que devolver el indice en el que esta la primera vez, y si NO esta -1

def buscar_entero_lista(values:list, target:int)->int:
    for i in range(len(values)): # xq quiero ver cada posicion en la lista
        if values[i] == target: # Si o Si con i porque tenemos que recorrer el indice
            return i
    raise ValueError(f"{target} NO esta en lista")

def ordenar_lista_ascendente(lista:list)->None: 
    for i in range(len(lista) - 1):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]: # Ordena de forma ASCENDENTE
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def ordenar_lista_descendente(lista:list)->None: 
    for i in range(len(lista) - 1):
        for j in range(i+1, len(lista)):
            if lista[i] < lista[j]: # Ordena de forma ASCENDENTE
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def ordenar_lista(lista:list, ascendente:bool = True)->None:
    if ascendente:
        print(ordenar_lista_ascendente)
    else:
        print(ordenar_lista_descendente)

def contar_en_lista(lista:list, target:any)->int: # Cuantas veces esta target en la lista
    contador = 0
    for elemento in lista:
        if elemento == target:
           contador += 1
    return contador

def sumar_lista(lista:list)->int: #recibe una lista, y retorna la suma de los elementos

    total = 0
    for element in lista:
        total += element
    return total

def promediar_lista(lista:list)->float:
    if isinstance(lista, list):
        tam = len(lista)
        if tam != 0:
            return sumar_lista(lista)/ tam
        raise ValueError("No esta definido el promedio de una lista vacia")
    raise TypeError("Eso no es una lista")


def sorteador(lista:list):
    import time #: Esto es para que tarde un poco antes de resolver la funcion
    from random import randint
    print("The winner is ---> ")
    time.sleep(5) #--> esto es la cantidad de tiempo que quiero que tarde
    
    ganador = lista[randint(0, len(lista)-1)]
    print(ganador)
    # print(f"{lista[randint(0, len(lista)-1)]}")

