

def resto_division(dividendo: int, divisor: int)->int:
    """Calcula el resto de la division entera entre dos numeros

    Args:
        dividendo (int): dividendo
        divisor (int): divisor

    Returns:
        int: Resto de la division entera
    """
    return dividendo - (dividendo // divisor * divisor)

#---------------------------------------------------------------

print(resto_division(9,2))

