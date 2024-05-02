# todas las definiciones de las funciones van arriba

# definicion de la funcion: (anotation)
def sumar(a:int, b:int)->int :
    # Documentacion
    """suma de dos numeros enteros 

    Args:
        a (int): primer numero a sumar
        b (int): segundo numero a sumar

    Returns:
        int: resulado de sumar a y b 
    """
    return a + b


# firma de la funcion tiene: como se llama, que recibe, que devuelve --> sumar(a:int, b:int)

#--------------------------------------------------

# TAREA: pedir dos numeros enteros por consola, sumarlos y mostrar el resulado

def sumar(a:int, b:int)->int:
    # Tiene que pedir todo desde consola y mostrar desde consola
    # Es la mas reutilizable. Podemos usar su resultado
    # Las funciones tienen que hacer UNA SOLA COSA a la vez, y sino hay que descomponerlas en varias funciones
    pass

#--------------------------------------------------

print(sumar(5,6))

#--------------------------------------------------

#funcion help: para saber la documentacion de la funcion
    # help(sumar) #--> solo le pongo el nombre de la funcion

