


# FORMA ROBUSTA -----

def factorial(n:int)->int:
    """Calcular el factorial de un numero

    Args:
        n (int): numero para calcular el factorial

    Raises:
        ValueError: Lanza la exception si n NO es un numero natural

    Returns:
        int: El factorial de n 
    """
    if n < 0:
        raise ValueError("El factorial es solo para numeros naturales")
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact 

# -----------------

numero = 5
try:
    print(factorial(numero))
except ValueError as e:
    print(e) 