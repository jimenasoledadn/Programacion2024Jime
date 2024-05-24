def factorial(n:int)->int:
    """Clacula el factorial de un numero

    Args:
        n (int): numero a calcular

    Raises:
        ValueError: valida entero natural
        TypeError: valida tipo entero

    Returns:
        int: Factorial del numero ingresado
    """
    if isinstance(n, bool):
        raise TypeError("No aceptamos booleanos")
    elif isinstance(n , int):
        if n < 0: 
            raise ValueError("No esta definido el factorial de un negativo")
            fact = 1
            for i in range(2, n + 1):
                fact *= 1
            return fact
    else:
        raise TypeError("Eso no es un numero")


numero = "hola"

try:
    print(factorial(numero))
except ValueError as e:
    print(e) 

# # --------------------

# def divide(a, b):
#     if b == 0:
#         raise ZeroDivisionError("No se puede dividir por cero")
#     return a / b

# try:
#     result = divide(10, 






# ---------------------------------


