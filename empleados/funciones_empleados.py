from random import randint, choice
from data_empleados import *

# Choice: es para tirarle una lista y que elija cualquier elemento

# def buscar_entero_lista(values:list, target:int)->int:
#     for i in range(len(values)): # xq quiero ver cada posicion en la lista
#         if values[i] == target: # Si o Si con i porque tenemos que recorrer el indice
#             return i
#     raise ValueError(f"{target} NO esta en lista")

# def entero_in_lista(values:list, target:int)->bool:
#     try:
#         buscar_entero_lista(values, target)
#         return True
#     except: # Si NO voy a hacer uso de la excepcion SOLO dejo except solo
#         return False

# def cargar_lista_legajos(lista:list, cantidad:int):
#     from random import randint
#     LEGAJO_MIN = 20000
#     LEGAJO_MAX = 30000
#     while cantidad > 0:
#         legajo = randint(LEGAJO_MIN, LEGAJO_MAX) # pido el legajo
#         if not entero_in_lista(lista,legajo):
#             lista.append(legajo)
#             cantidad -= 1

def validar_entero(numero:str)->bool:
    return numero.isalnum()

def cargar_lista_empleados_random(lista:list, cantidad:int)->None: # cantidad: es la cant de empleados
    next_legajo = 20000
    # UNA FORMA:
        # Le digo a la computadora que elija de forma aleatoria de una lista de valores (en este caso f y m) un genero, y lo guardo en la variable genero
        # Para que coincida el genero con el nombre, le digo a la maquina que elija un nombre pero de la lista de masculino o femenino 
    for _ in range(cantidad):
        legajo = next_legajo
        next_legajo += 1
        genero = choice(['f','m'])
        if genero == 'm':
            nombre = choice(nombres_m)
        else:
            nombre = choice(nombres_f)
        apellido = choice(apellidos)
        calle = f"calle {randint(1, 100)} nro {randint(100, 300)}"
        localidad = choice(localidades)
        provincia = choice(provincias)
        email = f"{nombre.lower()}{apellido.lower()}{choice(dominios)}"
        sector = choice(sectores)
        sueldo = float(randint(2000, 5000))
        lista.append(new_empleado(legajo, nombre, apellido, genero, calle, localidad, provincia, email, sector, sueldo ))

def new_empleado(legajo:int, nombre:str, apellido:str, genero:str, calle:str, localidad:str, provincia:str, email:str, sector:str, sueldo:float)->dict:
    empleado = {}
    empleado['legajo'] = legajo
    empleado['nombre'] = nombre
    empleado['apellido'] = apellido
    empleado['genero'] = genero
    empleado['calle'] = calle
    empleado['localidad'] = localidad
    empleado['provincia'] = provincia
    empleado['email'] = email
    empleado['sector'] = sector
    empleado['sueldo'] = sueldo 
    return empleado

def mostrar_empleados(lista_empleados: list)->None:
    tam = len(lista_empleados)
    print("                                                       *** Listado de Empleados ***            ")
    print(" --------------------------------------------------------------------------------------------------------------------------------------------------------- ")
    print(" Legajo      Nombre    Apellido   Genero       Calle              Localidad         Provincia                    Email                   Sector   Sueldo   ")
    print(" --------------------------------------------------------------------------------------------------------------------------------------------------------- ")
    for i in range(tam): 
        mostrar_empleado_item(lista_empleados[i])
    print()

def mostrar_empleado_item(unEmpleado: dict):
    print(f"  {unEmpleado['legajo']} {unEmpleado['nombre']:>10} {unEmpleado['apellido']:>10}      {unEmpleado['genero']:2}    {unEmpleado['calle']:>17}   {unEmpleado['localidad']:>15} {unEmpleado['provincia']:>15}  {unEmpleado['email']:>31}  {unEmpleado['sector']:>15}  {unEmpleado['sueldo']:7.2f}") 

def mostrar_empleado(unEmpleado: dict):
    print(f"Legajo: {unEmpleado['legajo']}\nNombre: {unEmpleado['nombre']}\nApellido: {unEmpleado['apellido']}\nGenero: {unEmpleado['genero']}\nDireccion: {unEmpleado['calle']} {unEmpleado['localidad']} {unEmpleado['provincia']}\nEmail: {unEmpleado['email']}\nSector: {unEmpleado['sector']}\nSueldo: ${unEmpleado['sueldo']:.2f}") 

# UNA FORMA: (con break)
    # Mirar como hizo Alejo en los primeros minutos para la validacion
def buscar_empleado_legajo_lineal(lista:list, legajo:int)->dict: # Si hay uno que existe devuelvo los datos. Y sino devuelve empleado vacio
    empleado = {} # Si el empleado no existe o no, ver como hacer o con una exception
    for emp in lista:
        if emp ["legajo"] == legajo:
            empleado = emp
            break
    return empleado
    # OTRA FORMA: (sin break):

def buscar_empleado_legajo_lineal_sin_break(lista:list, legajo:int)->dict:
    indice = 0 # 
    tam = len(lista)
    # Como no se en donde voy a encontrar el buscado, podria usar un While:
    while indice < tam and legajo != lista[indice]["legajo"]: # Mientras NO hayamos llegado al final de las lista y los legajos de la lista sean diferentes del legajo del empleado buscado
        indice += 1
    return {} if indice == tam else lista[indice]
    # if indice == tam:
    #     return {}
    # else:
    #     return lista[indice]

# Para usar esta busqueda tiene que estar SI o SI ordenada la lista
def buscar_empleado_legajo_binaria(lista: list, legajo: int)->dict:
    inf = 0
    sup = len(lista) - 1 
    while inf <= sup:                   
        medio = (inf + sup) // 2          
        if legajo == lista[medio]["legajo"]:  # Cuando comparamos legajo == con el legajo de un empleado (target) => lista[medio] -> me devuelve el empleado que esta en la posicion/indice: 'medio' de la lista Lista, (es un diccionario, es un empleado); Y lo que quiero de esa lista en esa posicion es el 'Legajo', entonces lo pongo ["legajo"]
            return lista[medio]                      
        elif legajo > lista[medio]["legajo"]:         
            inf = medio + 1                     
        else:                                 
            sup = medio - 1                    
    # raise ValueError(f"{legajo} is not in list")
    return {}

def swap_lista(lista:list, i:int, j:int)->None:
    aux =lista[i]
    lista[i] = lista[j]
    lista[j] = aux

def ordenar_empleados(empleados:list, campo:int, asc:bool = True):
    tam = len(empleados) # Podriamos armar una validacion que si no es ningun campo de los mencionados que tire una exception de tipo ValueError y un msje de campo invalido
    for i in range(tam - 1):
        for j in range(i + 1, tam ):
            if empleados[i][campo] > empleados[j][campo] if asc else empleados[i][campo] < empleados[j][campo]: 
                swap_lista(empleados, i, j)

# 1a-del profe
def mapear_nombres_sectores(lista:list)->list:
    lista_mapeada = []
    for el in lista:
        lista_mapeada.append([el["nombre"], el["sector"]])
    return lista_mapeada

# 4
def mapear_sectores(lista:list)->list:
    lista_mapeada = []
    for el in lista:
        lista_mapeada.append(el["sector"])
    return lista_sin_repetidos(lista_mapeada)

def lista_sin_repetidos(lista_repetidos:list)->list:
    return list(set(lista_repetidos)) # me pasan una lista con valores repetidos, lo convierto en un SET (que NO admite repetidos) con un solo elemento de cada valor repetido  (con la funcion set) ; y con la funcion list, lo vuelvo a convertir en una lista pero esta es SIN repetidos

# 1b-de un compañero:
def mostrar_empleados_nombre_sector(empleados:list):
    print("** Listado de empleados **  ")
    print("  Nombre  |  Sector ")
    print(" ------------------- ")
    for empleado in empleados:
        print(f"{empleado["nombre"]:^10} | {empleado["sector"]:^12}")

# 2 
def filtrar_empleados_sector(lista:list, sector:str)-> list:
    lista_filtrada = []
    for el in lista: 
        if el["sector"] == sector:
            lista_filtrada.append(el)
    return lista_filtrada



#3
def promedio_campo_empleados(lista:list, campo:str)->float:
    acumulador = 0
    cantidad = len(lista)
    if cantidad > 0:
        for empleado in lista:
            acumulador += empleado[campo]
        return acumulador / cantidad
    return 0.0

def promedio_sueldo_empleados(lista:list):
    return promedio_campo_empleado(lista, "sueldo")

def promedio_edad_empleados(lista:list):
    return promedio_campo_empleado(lista, "edad")
     

# -------------------- FUNCION LAMBDA ----------

# Retorna lo que pide la condicion SIN modificar al elemento
def filter_empleados(filtradora, lista: list)->list:
    lista_filtrada = []
    for el in lista: 
        if filtradora(el):
            lista_filtrada.append(el)
    return lista_filtrada

# ------------------

def promedio_sueldo_empleados(lista:list):
    return promedio_campo_empleados(lista, "sueldo")

def promedio_edad_empleados(lista:list):
    return promedio_campo_empleados(lista, "edad")

# Aca si hay una lista de 40 empleados, retorna una lista de la misma cantidad, 40 empleados. Esta funcion recibe un empleado, y hace lo que dice la funcion mapeadora, y lo retorna asi modificado
def mapear_empleados(mapeadora, lista:list)->list:
    lista_retorno = []

    for el in lista:
        x = mapeadora(el) # le pasamos cada empleado a mapeadora
        lista_retorno.append(x)  # aca va a guardar lo que nos devuelva mapeadora
        # lista.retorno.append(mapeadora(el)) -> 

    return lista_retorno

# ----------------- FUNCION EACH (cada): -------------

def each_empleado(funcion, lista:list)->None:
    for el in lista:
        funcion(el)


def ordenar_empleados_lambda(criterio, empleados:list):
    tam = len(empleados) # Podriamos armar una validacion que si no es ningun campo de los mencionados que tire una exception de tipo ValueError y un msje de campo invalido
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if criterio(empleados[i], empleados[j]): # criterio va a recibir a 2 empleados
                swap_lista(empleados, i, j)

def ordenar_lista(criterio, lista:list):
    tam = len(lista) # Podriamos armar una validacion que si no es ningun campo de los mencionados que tire una exception de tipo ValueError y un msje de campo invalido
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if criterio(lista[i], lista[j]): # criterio va a recibir a 2 empleados
                swap_lista(lista, i, j)

#5
def reduce_lista(funcion, lista:list):
    ant = lista[0]
    for i in range(1, len(lista)):
        ant = funcion(ant, lista[i])
    return ant

def reduce(funcion, lista:list): # 
    pass


