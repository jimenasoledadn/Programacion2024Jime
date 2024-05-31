from funciones_dict_alumnos_C13 import *

def calcular_promedio(a,b)->float:
    return (a+b)/2




def mostrar_alumnos(lista_alumnos: list)->None:
    tam = len(lista_alumnos)
    print("        *** Listado de Alumnos ***   ")
    print(" ---------------------------------------------------- ")
    print(" Legajo      Nombre  Genero  Nota 1   Nota 2   Promedio ")
    print(" ---------------------------------------------------- ")
    for i in range(tam): 
        mostrar_alumno(lista_alumnos[i])
    print()

def mostrar_alumno(unAlumno: dict):
    print(f"  {unAlumno['legajo']}  {unAlumno['nombre']:>10}      {unAlumno['genero']:2}     {unAlumno['nota_p1']:^2}       {unAlumno['nota_p2']:2}      {unAlumno['promedio']:5.2f}") # las posiciones de cada indice corresponde al dato que queremos obtener en cada llamada a la funcion ( 0:legajo, 1:nombre, 2:genero, 3:nota1, 4:nota2, 5:promedio)


    # Tengo que tener una funcion para validar cada dato: se llaman SETERS. Ejemplo:
def validar_legajo(legajo:int)->bool:
    LEGAJO_MIN = 20000
    LEGAJO_MAX = 30000
    # aca estoy validando solo que este en el rango. Habria que  queagregar sea un entero y no un string o booleano --> Esto ANTES de llegar al programa principal
        # Puedo hacer asi: return legajo >= LEGAJO_MIN and legajo <= LEGAJO_MAX
    # Otra forma:
    if legajo >= LEGAJO_MIN and legajo <= LEGAJO_MAX:
        return True
    raise ValueError("Legajo invalido")



    

# TENGO QUE TENER UN VALIDAR PARA CADA UNO: legajo, nombre, genero, y los demas







# --------------------------------------------    
    
# alumnos = [[28787,      "Juan", "m",  3 ,        4 ,      3.50],
#         [24862,     "Laura",  "f",   7   ,      4   ,    5.50],
#         [23046,     "Pedro" , "m",    6    ,    10    ,   8.00],
#         [27880,     "Sofía"  , "f",    1     ,    6    ,   3.50],
#         [27142,     "Diego",  "m",    1      ,   5    ,   3.00],
#         [26154,     "María",  "f",    3       ,  8    ,   5.50],
#         [21128,    "Carlos", "m",     5    ,     5     ,  5.00],
#         [21783,       "Ana",  "f",    7    ,     5    ,   6.00],
#         [27935,     "Luisa",  "f",    9    ,     8    ,   8.50],
#         [26029,    "Javier",  "m",    9    ,     8    ,   8.50]]
  
alumnos = []
TAM = 7

# for _ in range(TAM):
    # alumno = {} # 1) Asi creo un Diccionario vacio
    # # 2) Primero guardo todo en un auxiliar para poder validar todo lo que sea de ese legajo
    #         # Esto podria ser reemplazado por la funcion new_alumno
    # aux = (int(input("Ingrese legajo: ")))
    # alumno['legajo'] = aux # Ya lo asigno una vez que este validado
    # aux = ((input("Ingrese nombre: ")))
    # alumno['nombre'] = aux
    # aux = ((input("Ingrese genero: ")))
    # alumno['genero'] = aux
    # aux = (int(input("Ingrese nota parcial 1: ")))
    # alumno['nota_p1'] = aux
    # aux = (int(input("Ingrese nota parcial 2: ")))
    # alumno['nota_p2'] = aux

    # alumno['promedio'] = (calcular_promedio(alumno['nota_p1'], alumno['nota_p2']))


    
    # legajo = (int(input("Ingrese legajo: ")))
    # nombre = ((input("Ingrese nombre: ")))
    # genero = ((input("Ingrese genero: ")))
    # nota_p1 = int(input("Ingrese nota parcial 1: "))
    # nota_p2 = int(input("Ingrese nota parcial 2: "))

    # alumnos.append(new_alumno(legajo, nombre, genero, nota_p1, nota_p2))


cargar_alumnos_random(alumnos, TAM)

# mostrar_alumnos(alumnos)
# ordenar_alumnos(alumnos)
# mostrar_alumnos(alumnos)

# -------------

# mostrar_alumnos(alumnos)

# ordenar_alumnos(alumnos, "genero", asc=False) # Genero descendente
# mostrar_alumnos(alumnos)

# ordenar_alumnos(alumnos, "legajo") # Legajo ascendente
# mostrar_alumnos(alumnos)

# ordenar_alumnos(alumnos, "promedio", asc=False) # promedio descendente
# mostrar_alumnos(alumnos)

# -----------------

mostrar_alumnos(alumnos)

ordenar_alumnos(alumnos, "genero", asc=False) 
mostrar_alumnos(alumnos)

ordenar_alumnos_genero_legajo(alumnos)
mostrar_alumnos(alumnos)
