from random import randint, choice
from data_empleados_C13 import *

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

def cargar_lista_empleados_random(lista:list, cantidad:int)->None: # cantidad: es la cant de empleados
    next_legajo = 200000
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
        mostrar_empleado(lista_empleados[i])
    print()

def mostrar_empleado(unEmpleado: dict):
    print(f"  {unEmpleado['legajo']} {unEmpleado['nombre']:>10} {unEmpleado['apellido']:>10}      {unEmpleado['genero']:2}    {unEmpleado['calle']:>17}   {unEmpleado['localidad']:>15} {unEmpleado['provincia']:>15}  {unEmpleado['email']:>31}  {unEmpleado['sector']:>15}  {unEmpleado['sueldo']:7.2f}") 
