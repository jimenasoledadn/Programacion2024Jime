
# UNA FORMA:
def buscar_empleado_legajo_lienal(lista:list, legajo:int)->dict: # Si hay uno que existe devuelvo los datos. Y sino devuelve empleado vacio
    empleado = {} 
    for emp in lista:
        if emp ["legajo"] == legajo:
            empleado = emp
    return empleado

# def busqueda_binaria(lista: list, target: int)->dict:
#     inf = 0
#     sup = len(lista) - 1 
#     while inf <= sup:
#         medio = (inf + sup) // 2
#         if target == lista[medio]:
#             return medio
#         elif target > lista[medio]:
#             inf = medio + 1
#         else:
#             sup = medio - 1 
#     raise ValueError(f"{target} is not in list")

# UNA FORMA:
    # Mirar como hizo Alejo en los primeros minutos para la validacion
def buscar_empleado_legajo_lineal(lista:list, legajo:int)->dict: # Si hay uno que existe devuelvo los datos. Y sino devuelve empleado vacio
    empleado = {} # Si el empleado no existe o no, ver como hacer o con una exception
    for emp in lista:
        if emp ["legajo"] == legajo:
            empleado = emp
            break
    return empleado

def swap_lista(lista:list, i:int, j:int)->None:
    aux =lista[i]
    lista[i] = lista[j]
    lista[j] = aux

def ordenar_empleados(empleados:list, campo:str, asc:bool = True):
    tam = len(empleados) # Podriamos armar una validacion que si no es ningun campo de los mencionados que tire una exception de tipo ValueError y un msje de campo invalido
    for i in range(tam - 1):
        for j in range(i + 1, tam ):
            if empleados[i][campo] < empleados[j][campo] if asc else empleados[i][campo] > empleados[j][campo]: 
                swap_lista(empleados, i, j)

# Para usar esta busqueda tiene que estar SI o SI ordenada la lista
def buscar_empleado_legajo_binaria(lista: list, target: int)->dict:
    inf = 0
    sup = len(lista) - 1 
    while inf <= sup:                   # 1) va a entrar si inf es menor a sup
        medio = (inf + sup) // 2           # 2) busco el punto medio -> el promedio
        if target == lista[medio]:         # 3) Comparo para ver si es el valor buscado
            return medio                        # Si es lo retorno
        elif target > lista[medio]:         # 4) Si el valor buscado es mayor al numero en el punto medio
            inf = medio + 1                     # El valor inferior pasaria a ser el punto medio mas +1
        else:                                 # SINO: Si el valor buscado es MENOR al numero en el punto medio:
            sup = medio - 1                     #  cambiaria el limite superior a ser el valor del medio, menos -1
    raise ValueError(f"{target} is not in list")    # Si NO encuentro el numero, informo



def promedio_campo_empleado(lista:list, campo:str)->float:
    acumulador = 0
    cantidad = len(lista)
    if cantidad > 0:
        for empleado in lista:
            acumulador += empleado[campo]
            return acumulador / cantidad
    return 0.0
















