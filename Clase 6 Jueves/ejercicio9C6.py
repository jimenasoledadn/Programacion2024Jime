def esMultiplo(a:int, b:int)->int:
    """Verifica si un numero es multiplo de otro

    Args:
        a (int): divisor
        b (int): multiplo

    Returns:
        int: True si b es multiplo de a, False caso contrario
    """
    return b % a == 0
    # Tmbien podemos reutilizar el codigo anterior de ejercicio9C5 .. de resto_division si estuviera en el mismo archivo
    # return resto_division(b,a) == 0
# ------------------------------------------

print(esMultiplo(4,20))
print(esMultiplo(4,21))

