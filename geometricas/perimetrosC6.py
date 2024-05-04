def calcularPerimetroCircunferencia(radio: float)->float:
    """Pide el valor del radio y calcula el perimetro

    Args:
        radio (float): valor del radio

    Returns:
        float: perimetro de la circunferencia
    """
    from math import pi
    return pi * radio * 2

def calcular_perimetro_rectangulo(base:float, altura:float)->float:
    return 2 * (base + altura)

def calcular_perimetro_cuadrado(lado:float)-> float:
    # Reutilizacion de codigo:
    return calcular_perimetro_rectangulo(lado, lado)
    # Sino tambien: return lado * 4