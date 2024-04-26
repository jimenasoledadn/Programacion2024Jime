


def in_interval(valor:int, inferior:int, superior: int)-> bool:
    """verifica si un entero esta dentro de un rango

    Args:
        valor (int): valor a verificar
        inferior (int): limite inferior del rango
        superior (int): limite superior del rango

    Returns:
        bool: True si el valor esta dentro del rango / Flase en caso contrario
    """
    # FORMA 1):
        # if(valor >= inferior and valor <= superior):
        #     return True
        # else:
        #     return False
    # FORMA 2):
        # afuera = False
        # if(valor >= inferior and valor <= superior):
        #     afuera = True

        # return afuera
    # FORMA 3):
    return valor >= inferior and valor <= superior
    
#--------------------------------------------------

print(in_interval(3,2,5))
print(in_interval(3,1,5))
print(in_interval(3,4,9))
print(in_interval(5,80,20))

#--------------------------------------------------

# FUNCION ROBUSTA: Que no haya margen de error, que se pueda validar todo 

#--------------------------------------------------

