# FUNCION QUE SUME 2 NUMEROS y mostrar el resultado por consola, utilizando una funcion


    # FORMA: 1
# def sumarDosEnteros() -> int:
#     x = int(input(("Ingrese el primer sumando: ")))
#     y = int(input(("Ingrese el primer sumando: ")))
#     suma = x + y
#     print(f"La suma de los dos numeros es: ", suma)

# sumarDosEnteros()


def sumarDosEnteros(x,y) -> int: # -> int = es para decirme el tipo de retorno que va a tener
    return x + y # Puedo usar este numero!


suma = sumarDosEnteros(4,5)
print(suma)


print(suma + 5) # Esto para mostrar que puedo reutilizar lo que me retorna la funcion.