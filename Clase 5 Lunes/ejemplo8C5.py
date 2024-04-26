

def out_interval(valor:int, inferior:int, superior: int)-> bool:
    """verifica si un entero esta fuera de un rango

    Args:
        valor (int): valor a verificar
        inferior (int): limite inferior del rango
        superior (int): limite superior del rango

    Returns:
        bool: False si el valor esta dentro del rango / True en caso contrario
    """
    numeroFueraDelRango = False
    if (valor <= inferior or valor >= superior ):
        numeroFueraDelRango = True
    return numeroFueraDelRango

print(out_interval(3,2,5))
print(out_interval(3,1,5))
print(out_interval(3,4,9))
print(out_interval(5,80,20))

