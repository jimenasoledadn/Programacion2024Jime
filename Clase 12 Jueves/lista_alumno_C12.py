LEGAJO = 0
NOMBRE = 1
GENERO = 2
NOTA_1 = 3
NOTA_3 = 4
PROMEDIO = 5


def calcular_promedio(a,b)->float:
    return (a+b)/2

def mostrar_alumnos(lista_alumnos: list)->None:
    tam = len(lista_alumnos)
    print("        *** Listado de Alumnos ***   ")
    print(" ---------------------------------------------------- ")
    print(" Legajo    Nombre  Genero  Nota 1   Nota 2   Promedio ")
    print(" ---------------------------------------------------- ")
    for i in range(tam): # Pongo cualquier proms ya que todas van a tener la misma cantidad de elementos
        mostrar_alumno(lista_alumnos[i])
    print()

def mostrar_alumno(unAlumno:list):
    print(f"  {unAlumno[LEGAJO]}{unAlumno[NOMBRE]:>10}     {unAlumno[GENERO]:2}     {unAlumno[NOTA_1]:^2}      {unAlumno[NOTA_2]:2}      {unAlumno[PROMEDIO]:5.2f}") # las posiciones de cada indice corresponde al dato que queremos obtener en cada llamada a la funcion ( 0:legajo, 1:nombre, 2:genero, 3:nota1, 4:nota2, 5:promedio)


# --------------------------------------------


alumnos = [[28787,      "Juan", "m",  3 ,        4 ,      3.50],
        [24862,     "Laura",  "f",   7   ,      4   ,    5.50],
        [23046,     "Pedro" , "m",    6    ,    10    ,   8.00],
        [27880,     "Sofía"  , "f",    1     ,    6    ,   3.50],
        [27142,     "Diego",  "m",    1      ,   5    ,   3.00],
        [26154,     "María",  "f",    3       ,  8    ,   5.50],
        [21128,    "Carlos", "m",     5    ,     5     ,  5.00],
        [21783,       "Ana",  "f",    7    ,     5    ,   6.00],
        [27935,     "Luisa",  "f",    9    ,     8    ,   8.50],
        [26029,    "Javier",  "m",    9    ,     8    ,   8.50]]
  

mostrar_alumnos(alumnos)


