def sumar(a:int, b:int)->int :
    # Documentacion
    """suma de dos numeros enteros 

    Args:
        a (int): primer numero a sumar
        b (int): segundo numero a sumar

    Returns:
        int: resulado de sumar a y b 
    """
    if not isinstance(a, int):
        raise ValueError("El primer operando debe ser un numero")
    if not isinstance(b, int):
        raise ValueError("El segundo operando debe ser un numero")
    
    return a + b   

def restar(a:int, b:int)->int :
    # Documentacion
    """Resta de dos numeros enteros 

    Args:
        a (int): primer numero a restar
        b (int): segundo numero a restar

    Returns:
        int: resulado de la resta entre a y b 
    """
    if not isinstance(a, int):
        raise ValueError("El primer operando debe ser un numero")
    if not isinstance(b, int):
        raise ValueError("El segundo operando debe ser un numero")

    return a - b

def dividir(a:int, b:int)->float:
    return a / b

def multiplicar(a:int, b:int)->int:
    """Multiplica los dos numeros que le llegan por parametro

    Args:
        a (int): multiplicando     
        b (int): multiplicador  

    Returns:
        int: el producto del multiplicador con el multiplicando
    """
    if not isinstance(a, int):
        raise ValueError("El primer operando debe ser un numero")
    if not isinstance(b, int):
        raise ValueError("El segundo operando debe ser un numero")

    return a * b 

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
        for i in range(1, n + 1):
            fact *= i
        return fact
    else:
        raise TypeError("Eso no es un numero") 




# -------------------------




x = int(input("Ingrese primero operando A: "))

y = int(input("Ingrese segundo operando B: "))






# resultado_resta = restar(x,y)
# resultado_division = dividir(x,y)
# resultado_multiplicacion = multiplicar(x,y)
# resultado_factorial_A = factorial(x)
# resultado_factorial_B = factorial(y)


# RESPUESTAS





# resultado_suma = sumar(x,y)
# print(f"El resultado de {x} + {y} es: {resultado_suma} ")

# print(f"El resultado de {x} - {y} es: {resultado_resta} ")
# print(f"El resultado de {x} / {y} es: {resultado_division:.2f} ")
# print(f"El resultado de {x} * {y} es: {resultado_multiplicacion} ")
# print(f"El factorial de {x} es: {resultado_factorial_A}; y El Factorial de {y} es: {resultado_factorial_B} ")

