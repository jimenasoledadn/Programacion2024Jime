# --------------- PARADIGMA FUNCIONAL -----------------

# Los lenguajes que sus funciones son ciudadanos de primera clase porque pueden implementar estos 3 conceptos, se dice que estos lenguajes implementan el paradigma funcional
# Se dice que en este paradigma la funcion son ciudadanos de primera clase, por 3 motivos:
        #1- Una funcion se puede asignar a una variable.

def sumar(a,b):
    return a+b
print(sumar) # -> me dice que es de tipo funcion, nombre sumar, y la direccion de memoria de la funcion en hexadecimal (esta en el segmento de codigo esta direccion)
print(sumar(3,4)) # llamada a la funcion: = 7
print(type(sumar)) # me da el tipo: class function .. de tipo funcion

unaFuncion = sumar # Estoy asignando la direccion de memoria de la funcion a OTRA variable. (sin poner parentesis es la direccion, Con parentesis es Llamada a la funcion)
print(unaFuncion(3,5)) # sumar = unaFuncion : las dos guardan la misma direccion de memoria, asi que podemos llamar a la funcion de cualquiera de las 2 variables
print("---------")
        # ---------------------------------------------------------------- #
        #2- Una funcion se puede pasar como argumento a otra funcion. Se le puede pasar como parametro para decirle en tiempo de ejecucion como se tiene que comportar. 
        # Con esto logro hacer ASINCRONISMO (mejor explicacion en 00:35)

def saludar():
    print("Hola")
def despedir():
    print("Chau")

def ejecutora(una_funcion):
    una_funcion()

def restar(a,b):
    return a-b
def multiplicar(a,b):
    return a*b
def dividir(a,b):
    if b != 0:
        return a/b
    raise ValueError("No se puede dividir por cero")

def operar(operacion, op1, op2):
    return operacion(op1, op2)
# --------
n1 = 7
n2 = 5
# ejecutora(saludar)
# ejecutora(despedir)

print(operar(sumar, n1, n2))
print(operar(restar, n1, n2))
print(operar(multiplicar, n1, n2))
print(operar(dividir, n1, n2))

print(" ------------- ")
        # ---------------------------------------------------------------- #
        #3- Una funcion puede retornar una/otra funcion
        # Esto se usa mucho en los modulos, o sea cuando importamos el archivo con todas las funciones, seria importar un archivos. Pero si solo importamos UNA sola funcion, es como hace esto- de un modulo importo una funcion

def fabrica_funciones(nombre:str):
    def restar(a,b):
        return a-b
    def multiplicar(a,b):
        return a*b
    def dividir(a,b):
        if b != 0:
            return a/b
        raise ValueError("No se puede dividir por cero")
    match nombre:
        case "restar" : return restar
        case "multiplicar" : return multiplicar
        case "dividir" : return dividir

# ------------

x = fabrica_funciones("restar")
print(x(4,5))

x = fabrica_funciones("multiplicar")
print(x(4,5))

x = fabrica_funciones("dividir")
print(x(4,5))

# ------------------------ FUNCION LAMBDA ---------------------
print("--------------")

print(operar(sumar, n1, n2))
print("Forma LAMBDA: ")
print(operar(lambda a, b: a + b, n1, n2)) # funcion lambda se guarda en el                                    parametro operacion de la funcion operar
print(operar(lambda a, b: a * b, n1, n2))
print(operar(lambda a, b: a / b, n1, n2))

# --------------------

