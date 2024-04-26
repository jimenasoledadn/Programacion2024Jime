

def compararEnteros(a:int, b:int)->int: 
    """Compara dos numeros enteros

    Args:
        a (int): primero numero a comprar
        b (int): segundo numero a comparar

    Returns:
        int: -1 Si a es menor que b, 0 si a es igual a b, y 1 si a es mayor que b
    """
    if( a < b):
        comparacion = -1
    elif a == b :
        comparacion = 0
    else:
        comparacion = 1
    
    return comparacion

    # tambien:
        # retorno = 0

        # if a > b:
        #     retorno = -1
        # elif a > b:
        #     retorno = 1
        # return retorno
    


# implementar la funcion y escribir un programa que la testee
#--------------------------------------------------
# (se puede testear la funcion en solo una linea de codigo por ejemplo)
# Puedo utilizar varios return (o sea en cada comparacion) o asignar un valor, y retornar ese valor


primerNumero = int(input("Ingrese el primer numero a comprar: "))
segundoNumero = int(input("Ingrese el segundo numero a comprar: "))

print(compararEnteros(primerNumero, segundoNumero))

