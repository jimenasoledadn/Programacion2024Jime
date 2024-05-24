
# UNA FORMA:
def buscar_empleado_legajo_lienal(lista:list, legajo:int)->dict: # Si hay uno que existe devuelvo los datos. Y sino devuelve empleado vacio
    empleado = {} 
    for emp in lista:
        if emp ["legajo"] == legajo:
            empleado = emp
    return empleado

def busqueda_binaria(lista: list, target: int)->dict:
    inf = 0
    sup = len(lista) - 1 
    while inf <= sup:
        medio = (inf + sup) // 2
        if target == lista[medio]:
            return medio
        elif target > lista[medio]:
            inf = medio + 1
        else:
            sup = medio - 1 
    raise ValueError(f"{target} is not in list")


def promedio_campo_empleado(lista:list, campo:str)->float:
    acumulador = 0
    cantidad = len(lista)
    if cantidad > 0:
        for empleado in lista:
            acumulador += empleado[campo]
            return acumulador / cantidad
    return 0.0
















