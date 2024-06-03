# ------------------ FUNCIONES LAMBDA --------------------

# NO tienen nombre
# Estan pensadas para que sean cortas en una sola linea
# Es "parecido" a las formas del operador ternario

# Funcion "comun":
def sumar(a, b):
    return a + b

# para escribir una funcion anonima tengo que escribir la palabra lambda, los dos parametros, dos puntos y lo qe retorna:
lambda a, b: a + b # esto me devuelve la direccion de memoria de la funcion
                # para poder llamarla la tengo que asignar a una variable:
s = lambda a, b: a + b 
print(s(4,3))

# podria hacer: (esta con las demas funciones en ciudadano_primera_clasee.py)
# print(operar(lambda a, b: a+ b, n1, n2)) # funcion lambda se guarda en el                                    parametro operacion de la funcion operar

# ---------------------
print(" --- ")

def ejecutora_sin_parametros(funcion):
    funcion()

ejecutora_sin_parametros(lambda : print("Hola"))

