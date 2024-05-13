

def pedir_numero_rango(l_inf, l_sup, veces)->int:
    while veces > 0:
        numero = int(input(f"Ingrese un numero entre {l_inf} y {l_sup}: "))

        if numero < l_inf or numero > l_sup:
            print("Error. Fuera de rango")
            veces -= 1
        else:
            return numero
    raise ValueError("Demasiados intentos")

# ----------------

try:
    x = pedir_numero_rango(18, 65, 3)
    print(x)
except ValueError as e:
    print(e)
    exit()