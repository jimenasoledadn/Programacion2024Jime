
# Esta es la funcion menos reutilizable, xq tiene que encargarse de pedir los numeros, de sumarlos, y de mostrarlos, y NO podria tocar, customizar NADA
def sumar():
    pass

# Esta es la funcion MAS reutilizable. Recibe los dos enteros, adentro lo unico que hace es la suma y lo devuelve. Lo puedo usar en cualquier lado, lo que me devuelve lo puedo usar como quiero, y los datos tambien puedo conseguirlos como quiero
def sumar(a:int, b:int) -> int:
    pass

# SOLO puedo conseguir los datos como quiero, pero no podria utilizar el resultado xq NO ME LO RETORNA la funcion. 
def sumar(a:int, b:int):
    pass

# Se tiene qe encargar de pedir y sumar los datos. Solo me retorna el resultado
def sumar() -> int:
    pass



# MIRAR SI UNA FUNCION ESTA HACIENDO MAS DE UNA TAREA, HABRIA QUE DESCOMPONERLA: O SEA MODULARIZARLA para que 
# una vaya llamando a la otra