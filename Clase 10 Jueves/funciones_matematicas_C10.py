



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
    elif isinstance(n , int): # Discrimina si es una valor de tipo
        if n < 0: # Valida un error en el VALOR , de Value
            raise ValueError("No esta definido el factorial de un negativo")
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact
    else:
        raise TypeError("Eso no es un numero") # Me aparece el error por terminal

# isinstance = le paso un objeto y le paso una clase. Y me dice con un booleano si es de esa clase o no 
# -----------------------------------------------

try:
    print(factorial(5))
# except Exception as e: # Esto va a capturar cualquier tipo de error. Y abajo puedo armar un if (condicional) para cada tipo de error
#     print(e)
except ValueError as e:
    print("Ocurrio un error de tipo Value")
except TypeError as e:
    print(e) # muestra el msje



