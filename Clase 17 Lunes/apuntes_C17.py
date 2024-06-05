

# Con la extension es para saber con que se tendria que leer y por quien/quines puede ser abierto


# PARA DIFERENCIAR: python muestra con comillas simples los datos de un diccionario !!!! 



# ----------- INSERTION SORT -----------------

# el elemento seleccionado lo comparamos con el que esta a la izquierda, con los que estan ANTES (queda el hueco en donde se va a insertar)

mi_grupo = [4, 9, 2, 8, 5]

# 9 es menor a 4 .. NO .. sigue...
#     9 queda en el lugar, y el indice avanza

# 2 es menor a 9.. SI .. entonces cambia:
#     el 9 avanza una posicion, y el 2 retroce una posicion
mi_grupo = [4, 2, 9, 8, 5]
# 2 es mas chico que 4.. SI .. entonces cambia:
#     el 4 avanza, y el 2 retocede.. HASTA DONDE? --> Hasta que el elemento NO sea menor que el que esta atras o NO haya llegado al indice 0, porque ya no tiene mas con quien compararse
mi_grupo = [2, 4, 9, 8, 5]

# 8 es menor al 9.. Si .. Se va a insertar en donde encuentra un elemento que es mas chico.
mi_grupo = [2, 4, 8, 9, 5]

# 5 es menor a 9 .. __si
mi_grupo = [2, 4, 8, 5, 9]

# 5 es mas chico que 8 .. si 
mi_grupo = [2, 4, 5, 8, 9]

# 5 es mas chico que 4.. no.. se queda ahi:
mi_grupo = [2, 4, 5, 8, 9]




# --------
# Entonces hay diferentes tipos de ordenamiento:
        # bubble sort
        # insert sort
