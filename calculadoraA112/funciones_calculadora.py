def limpiar_pantalla():
    import os
    os.system("cls")

def pausar():
    import os
    os.system("pause")

def menu_calculadora()->str:
    """Muestra el menu de opciones de la calculadora

    Returns:
        str: devuelve la opcion seleccionada
    """
    limpiar_pantalla()
    print(f"{'Calculadora':^25s}")
    print(f"{'-----------':^25s}") 
    print(" Opciones: ")
    print("1- Ingresar 1er operando A: ")
    print("2- Ingresar 2do operando B: ")
    print("3- Calcular todas las operaciones ")
    print("4- Informar resultados")
    print("5- Salir")

    return input("Ingrese opcion: ")

def pedir_operando_primero()->int:
    """Pide un numero por consola y lo convierte en entero, para luego retornarlo

    Raises:
        ValueError: valida que sea un entero natural

    Returns:
        int: retorna un entero
    """
    operando = int(input("A: "))
    if isinstance(operando, int):
        return operando
    raise ValueError("Debe ingresar un numero")

def pedir_operando_segundo()->int:
    """Pide un numero por consola y lo convierte en entero, para luego retornarlo

    Raises:
        ValueError: valida que sea un entero natural

    Returns:
        int: retorna un entero
    """
    operando = int(input("B: "))
    if isinstance(operando, int):
        return operando
    raise ValueError("Debe ingresar un numero")

def pedir_confirmacion(mensaje:str)->bool: 
    rta = input(mensaje).lower()
    return rta == "s"

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