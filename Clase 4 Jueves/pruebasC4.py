


nombre = "Juan"
# print("nombre: ", nombre)
# print("nombre: " + nombre)
# print(f"Nombre: {nombre}")

# ----------------------------
#     # OPERADOR TERNARIO: 
# x = 1 if True else 0 # O: x = 1 if False else 0
# print(x)

# # -- 

# cantMasculinos = 0

# print(f"{cantMasculinos if cantMasculinos > 0 else "No hubo masculinos"}")

# -----------------------------------

            # CONTINUE:

    #   1) Me muestra los numeros del 0 al 9

contador = 0

while contador < 10:
    print(contador)
    contador += 1

print("Fin")

# -- 

    #   2) Me muestra del 0 al 4. Porque al llegar y contador == 5, el BREAK me va a eyectar hacia afuera del while. Es decir hara de 0 a 4, y luego 'Fin'

contador = 0

while contador < 10:
    if contador == 5:
        break
    print(contador)
    contador += 1

print("Fin")

# --

     #   3) CONTINUE: es parecido al break pero NO me saca del bucle. Va a mostrar todo, menos lo que haya en la condicion, y seguira en la repeticion del while hasta que se cumpla la condicion

contador = 0

while contador < 10:
    contador += 1
    if contador == 5:
        continue
    print(contador)

print("Fin")

# -- 

contador = 0

while contador < 10:
    contador += 1
    print(contador)
print("Fin")


# -------------------------------------------------------------
