#       Enunciado
# Hacer una calculadora. Para ello el programa iniciará y contará con un menú de opciones:
#   1. Ingresar 1er operando (A=x)
#   2. Ingresar 2do operando (B=y)
#   3. Calcular todas las operaciones
#       a) Calcular la suma (A+B)
#       b) Calcular la resta (A-B)
#       c) Calcular la división(A/B)
#       d) Calcular la multiplicación(A*B)
#       e) Calcular factorial(A!)
#   4. Informar resultados
#       a) “El resultado de A+B es: r”
#       b) “El resultado de A-B es: r”
#       c) “El resultado de A/B es: r” o “No es posible dividir por cero”
#       d) “El resultado de A*B es: r”
#       e) “El factorial de A es: r1 y El factorial de B es: r2”
#   5. Salir
# • Todas las funciones matemáticas del menú se deberán realizar en una biblioteca aparte,que contenga las funciones
#   para realizar las cinco operaciones.
# • En el menú deberán aparecer los valores actuales cargados en los operandos A y B(donde dice “x” e “y” en el ejemplo,
#   se debe mostrar el número cargado)
# • Deberán contemplarse los casos de error (división por cero, etc.)
# • Documentar todas las funciones

from funciones_calculadora import *

# -------------------------------
flag_primer_operando = False
flag_segundo_operando = False
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

            elif flag_primer_operando and flag_segundo_operando != True:
                print("Debe ingresar el segundo operando para continuar")
            else:
                print("Debe ingresar primero los dos operandos para continuar")
        case "4":
            print(f"El resultado de {x} + {y} es: {resultado_suma} ")
            print(f"El resultado de {x} - {y} es: {resultado_resta} ")
            print(f"El resultado de {x} / {y} es: {resultado_division:.2f} ")
            print(f"El resultado de {x} * {y} es: {resultado_multiplicacion} ")
            print(f"El factorial de {x} es: {resultado_factorial_A}; y El Factorial de {y} es: {resultado_factorial_B} ")
        case "5":
            if(pedir_confirmacion("Confirma salida?: s/n ")):
                seguir = "n"
            continue 
    pausar()

print("Fin del programa")