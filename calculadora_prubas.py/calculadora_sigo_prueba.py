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
    """Muestra un mensaje por pantalla para pedir confirmacion de salida del programa

    Args:
        mensaje (str): pregunta al usuario si quiere seguir en el programa o salir

    Returns:
        bool: indica la letra de salida
    """
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
    """ Division de dos numeros enteros

    Args:
        a (int): recien un numero entero, el dividendo
        b (int): recibe un segundo numero entero, el divisor

    Returns:
        float: Devuelve el resultado de la division, cociente
    """
    if b < 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    else:
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



# -------------------------------
flag_primer_operando = False
flag_segundo_operando = False
flag_opcion3_calcular = False
seguir = "s"



while seguir == "s":
    match menu_calculadora():
        case "1":
            try:
                x = pedir_operando_primero()
                flag_primer_operando = True
            except ValueError as e:
                print("Error. Debe ingresar un numero")

        case "2":
            if flag_primer_operando:
                try:
                    y = pedir_operando_segundo()
                    flag_segundo_operando = True
                except ValueError as e:
                    print("Error. Debe ingresar un numero") 
            else:
                print("Debe ingresar primero el primer operando")
            
        case "3":
            if flag_primer_operando and flag_segundo_operando:
                print(f"a- Calcular la suma de {x} + {y}: ")
                print(f"b- Calcular la resta de {x} - {y}: ")
                print(f"c- Calcular la división de {x} / {y}: ")
                print(f"d- Calcular la multiplicación de {x} * {y}: ") 
                print(f"e- Calcular factorial de {x}, y el factorial de {y}:")
                resultado_suma = sumar(x,y)
                resultado_resta = restar(x,y)
                resultado_division = dividir(x,y)
                resultado_multiplicacion = multiplicar(x,y)
                resultado_factorial_A = factorial(x)
                resultado_factorial_B = factorial(y)

                flag_opcion3_calcular = True

            elif flag_primer_operando and flag_segundo_operando != True:
                print("Debe ingresar el segundo operando para continuar")
            else:
                print("Debe ingresar primero los dos operandos para continuar")
        case "4":
            if flag_opcion3_calcular:
                print(f"El resultado de {x} + {y} es: {resultado_suma} ")
                print(f"El resultado de {x} - {y} es: {resultado_resta} ")
                print(f"El resultado de {x} / {y} es: {resultado_division:.2f} ")
                print(f"El resultado de {x} * {y} es: {resultado_multiplicacion} ")
                print(f"El factorial de {x} es: {resultado_factorial_A}; y El Factorial de {y} es: {resultado_factorial_B} ")
                flag_primer_operando = False
                flag_segundo_operando = False
                
            elif flag_primer_operando == True and flag_segundo_operando != True:
                print("Debes ingresar el segundo operando para poder continuar ")
            else:
                print("Debes ingresar los dos operando y realizar las operaciones para obtener los resultados")
        case "5":
            if(pedir_confirmacion("Confirma salida?: s/n ")):
                seguir = "n"
            continue 
    pausar()

print("Fin del programa")