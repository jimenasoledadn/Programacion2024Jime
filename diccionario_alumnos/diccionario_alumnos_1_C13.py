

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
TAM = 3

for _ in range(TAM):
    alumno = {} # 1) Asi creo un Diccionario vacio
    # 2) Primero guardo todo en un auxiliar para poder validar todo lo que sea de ese legajo
            # Esto podria ser reemplazado por la funcion new_alumno
    aux = (int(input("Ingrese legajo: ")))
    alumno['legajo'] = aux # Ya lo asigno una vez que este validado
    aux = ((input("Ingrese nombre: ")))
    alumno['nombre'] = aux
    aux = ((input("Ingrese genero: ")))
    alumno['genero'] = aux
    aux = (int(input("Ingrese nota parcial 1: ")))
    alumno['nota_p1'] = aux
    aux = (int(input("Ingrese nota parcial 2: ")))
    alumno['nota_p2'] = aux

    alumno['promedio'] = (calcular_promedio(alumno['nota_p1'], alumno['nota_p2']))
    alumnos.append(alumno)    # 4) y AL FINAL, cargamos todo en la lista de alumnoS, el diccionario alumnO



    # 3) vamos cargando todo en el diccionario alumno
    # 4) y AL FINAL, cargamos todo en la lista de alumnoS, el diccionario alumnO
    # 5) Hay que refactorizar la lista de mostrar alumnos, porqe tiene para mostrar una lista, y ahora debe mostrar un diccionario xq creamos un diccionario-- Lo que cambio es que entre [] guardabamos una variable, una costante, un numero que indicaba el indice. Y AHORA guardamos un STRING que sea el nombre de la CLAVE (ponerle comillas al nombre de la clave)

mostrar_alumnos(alumnos)

# la variable alumno es un diccionario:
alumno = alumnos[0]
    
    # Si yo quisiera el nombre de un alumno, en diccionarios tengo 2 formas de obtenerlo:
alumno.get('nombre')
alumno['nombre']

    # Para trabajar con Listas de Diccionario, seria trabajar con listas de objetos alumnoS. Ejemplo:
        # alumno.nombre # Asi directamente para acceder al nombre con el operador punto .


    # 6) Siempre tiene que haber doble validacion, tanto en la funcion como en el programa principal