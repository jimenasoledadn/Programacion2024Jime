from data_warehouse_C11 import *


    # Este tipo de funciones se llaman: FUNCIONES CONSTRUCTORAS, xq le paso los valores de los datos y este los crea, los valida, los carga y agrega los valores, y devuelve el alumno cargado
    # para generar UN alumno: Crea el diccionario, lo carga y lo devuelve:
def new_alumno(legajo:int, nombre:str, genero:str, nota_p1:int, nota_p2:int)->dict:
    alumno = {}
    # Una de las formas:
    alumno['legajo'] = legajo
    alumno['nombre'] = nombre
    alumno['genero'] = genero
    alumno['nota_p1'] = nota_p1
    alumno['nota_p2'] = nota_p2
    alumno['promedio'] = calcular_promedio(nota_p1, nota_p2) 
    return alumno


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

def cargar_lista_enteros_random(lista, cant, desde, hasta):
    from random import randint
    for _ in range(cant):
        lista.append(randint(desde, hasta)) # la funcion randint  

def calcular_promedio(a,b)->float:
    return (a+b)/2

def cargar_lista_promedios(lista_a:list, lista_b:list, lista_proms:list)->None:
    """Recibe 3 listas, LEE las 2 primeras e indice a indice calcula el promedio y lo guarda en el mismo indice en la lista de proms 

    Args:
        lista_a (_type_): recibe una lista
        lista_b (_type_): recibe otra lista
        lista_proms (_type_): lista vacia, que va a guardar el promedio de las dos listas anteriores
    """
    tam = len(lista_a)
    for i in range(tam):
        lista_proms.append(calcular_promedio(lista_a[i], lista_b[i]))

def cargar_lista_notas(lista, cantidad):
    cargar_lista_enteros_random(lista, cantidad, 0, 10)
    #   LLAMADA A LA FUNCION:
                # x = []
                # cargar_lista_notas(x,20)
                # print(x)

def cargar_lista_nombres(lista:list, nombres: list, cantidad:int)->None:
    for i in range(cantidad):
        lista.append(nombres[i])
    # lista.extend(nombres[:cantidad]) --> Una propiedad de las listas, propio de python. Tambien se puede hacer asi, usando el metodo extend que AGREGA una lista a OTRA lista.

# def cargar_lista_nombres(lista:list, nombres:list, cantidad:int):
    # print("------------------")
    # print("Al inicio de la funcion: ", id(lista), lista)

    # lista = nombres[:cantidad] # Aca con el = estoy pisando lo que recibimos y se le asigna una sublista. NO es como un append en donde CARGO elementos a la lista.
    # # print("Dentro de funcion ", lista) # Aca van a aparecerm los 10 primeros nombres. En cambio cuando printee en mi programa a la lista no nombres me va a aparecer VACIA, xq NOMBRES esta apuntando a otro lado.
    # print("Al final de la funcion: ", id(lista), lista)
    # print("------------------")

def cargar_lista_generos(lista:list, gender: list, cantidad:int)->None:
    for i in range(cantidad):
        lista.append(gender[i])

# Los legajos NO se pueden repetir
def cargar_lista_legajos(lista:list, cantidad:int):
    from random import randint
    LEGAJO_MIN = 20000
    LEGAJO_MAX = 30000
    # tengo que hacer algo cantidad de veces:
        # conseguir un numero entre LEGAJO_MIN y LEGAJO_MAX
            # Si no esta en la lista, lo agrego,
            # Y si esta, tengo que conseguir otro

    # for _ in range(cantidad):
    #     legajo = randint(LEGAJO_MIN, LEGAJO_MAX)
    #     while entero_in_lista(lista, legajo):
    #         legajo = randint(LEGAJO_MIN, LEGAJO_MAX)
    #     lista.append(legajo)
        # pido el dato
        # MIENTRAS el dato sea invalido...
        #   pido nuevamente el dato
        
        # uso el dato
    
    #       OTRA FORMA:
    while cantidad > 0:
        legajo = randint(LEGAJO_MIN, LEGAJO_MAX) # pido el legajo
        if not entero_in_lista(lista,legajo):
            lista.append(legajo)
            cantidad -= 1 # cada vez que consigo un dato, le descuento un legajo. hasta que se complete la cantidad que quiero
            #   LLAMADA A LA FUNCION:
                        # x = []
                        # cargar_lista_notas(x,20)
                        # print(x)


# def cargar_alumnos_random(legs:list, names:list,genders:list, notas_p1:list, notas_p2:list, promedios:list, cantidad:int):
#     cargar_lista_legajos(legs, cantidad)
#     cargar_lista_nombres(names, nombres, cantidad)
#     cargar_lista_generos(genders, generos, cantidad)
#     cargar_lista_notas(notas_p1, cantidad)
#     cargar_lista_notas(notas_p2, cantidad)
#     cargar_lista_promedios(notas_p1, notas_p2, promedios)

def cargar_alumnos_random(alumnos:list, cantidad:int):
    legs = []
    names = []
    genders = []
    notas_p1 = []
    notas_p2 = []

    # Con esto nos va todos los legajos en las listas vacias
    cargar_lista_legajos(legs, cantidad)
    cargar_lista_nombres(names, nombres, cantidad)
    cargar_lista_generos(genders, generos, cantidad)
    cargar_lista_notas(notas_p1, cantidad)
    cargar_lista_notas(notas_p2, cantidad)

    # Recorremos todos los vectores cargados, y creamos un alumno con cada uno de esos datos
    for i in range(cantidad):
        alumnos.append(new_alumno(legs[i], names[i], genders[i], notas_p1[i], notas_p2[i]))

def obtener_lista_promedios(lista_a:list, lista_b:list, lista_proms: list)-> None:
    tam = len(lista_a)
    for i in range(tam):
        lista_proms.append(calcular_promedio(lista_a, lista_b))

def mostrar_alumnos(legs, names, genders, n1, n2, proms):
    print("        *** Listado de Alumnos ***   ")
    print(" ---------------------------------------------------- ")
    print(" Legajo    Nombre  Genero  Nota 1   Nota 2   Promedio ")
    print(" ---------------------------------------------------- ")
    for i in range(len(legs)): # Pongo cualquier proms ya que todas van a tener la misma cantidad de elementos
        mostrar_alumno(legs[i], names[i], genders[i], n1[i], n2[i], proms[i])
    print()

def mostrar_alumno(legajo:list, nombre:list, genero:list, n1:list, n2:list, promedio:list):
    print(f"  {legajo}{nombre:>10}     {genero:2}     {n1:^2}      {n2:2}      {promedio:5.2f}") # :5.2f --> 5 es el ancho de columna, el punto referencia a la parte decimal a la derecha, 2 la cantidad decimal que quiero, f especifica que es un flotante

def swap_lista(lista:list, i:int, j:int)->None:
    aux =lista[i]
    lista[i] = lista[j]
    lista[j] = aux

         # Para ordenar un dato en particular, si o si hay que ordenar el de todos los items, ya que sino quedarian defasados mezclados un dato con otro de un mismo alumno por ejemplo
    # def ordenar_alumnos(alumnos:list):
    #     tam = len(alumnos) # Hacemos esto para no tener que llamar a la funcion len en todo momento. Directamente lo guardamos en una         variable
    #     for i in range(tam - 1):
    #         for j in range(i+1, tam ):
    #             if alumnos[i]["promedio"] < alumnos[j]["promedio"]: # alumnos[i] --> esto es un elemento de la lista. La lista es de                 diccionarios alumnos, entonces ES un diccionario que guarda los datos de un alumno. Como quiero acceder al promedio          (para ordenarlos de forma ascendente en este caso), ingreso el campo promedio --> ["promedios"]

    #                 swap_lista(alumnos, i, j) # Aca intercambia el dato que tengo en la posicion i de la lista de diccionario, con la                     posicion j de la lista de diccionario
                    

def ordenar_alumnos(alumnos:list, campo:str, asc:bool = True):
    tam = len(alumnos) # Podriamos armar una validacion que si no es ningun campo de los mencionados que tire una exception de tipo ValueError y un msje de campo invalido
    for i in range(tam - 1):
        for j in range(i + 1, tam ):
            if alumnos[i][campo] < alumnos[j][campo] if asc else alumnos[i][campo] > alumnos[j][campo]: 
                swap_lista(alumnos, i, j)

# La idea seria que el primer criterio tenga algo que tengan todos en comun, de agrupamiento. Y el segundo como un desempate.. ejemplo:
def ordenar_alumnos_genero_legajo(alumnos: obtener_lista_promedios):
    tam = len(alumnos) 
    for i in range(tam - 1):
        for j in range(i + 1, tam ):
            # Si son del mismo genero:
            if alumnos[i]["genero"] == alumnos[j]["genero"]: # Si son iguales, los tengo que comparar AHORA por legajo:
                # Me fijo si estan desordenados por legajo
                if alumnos[i]["legajo"] > alumnos[j]["legajo"]: # quiero que se ordenen de forma ascendente (cuando sean 2 varones o dos mujeres --> primer condicion!!!)
                    swap_lista(alumnos, i, j)
            # Me dijo si estan desordenados por genero 
            elif alumnos[i]["genero"] > alumnos[j]["genero"]:  # Quiero preguntar ACA, si NO son del mismo genero, pregunto si estar ordenados y de ahi los los ordeno por: f (ascendente), o 'm': (descendente)
                swap_lista(alumnos, i, j)






            # if alumnos[i][campo] < alumnos[j][campo] if asc else alumnos[i][campo] > alumnos[j][campo]: 
            #     swap_lista(alumnos, i, j)