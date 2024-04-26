

def duplicar(a:int)->int: 
    """duplicar el valor ingresado

    Args:
        a (int): entero a duplicar

    Returns:
        int: devuelve el doble del valor ingresado
    """

    return a * 2 # a + a 

    # OTRA FORMA:
        # valorDuplicado = a * 2
        # return valorDuplicado


#--------------------------------------------------


valorIngresado = int(input("Ingrese el valor a duplicar: "))
# x = duplicar(5)
# print(x)

print(duplicar(valorIngresado)) # aca le estoy pasando a print el resultado de la funcion duplicar.
                                    # y print solo muestra por pantalla
                                # Se denomina, COMPOSICION DE FUNCIONES. que una funcion este dentro
                                    # de la otra

#--------------------------------------------------

# argumento / parametro

    # argumento es el valor que le passamos al llamar a la funcion
    # parametro es lo que va en la funcion
    # El parametro RECIBE al argumento

    # En este ejemplo, la a (a:int) --> es el parametro
    # La x es el argumento, en realidad es el valor que tenga la variable x !!!!!
