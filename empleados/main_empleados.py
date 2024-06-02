from funciones_empleados import *


TAM = 30
empleados = []

cargar_lista_empleados_random(empleados, TAM)

mostrar_empleados(empleados)
print("-----------")
print("-----------")



#0 pedir un legajo y mostrar al empleado con ese legajo

    # legajo = input("Ingrese legajo: ")

    # empleado = buscar_empleado_legajo_lineal(empleados, 20001)

    #     # Una forma de saber si un empleado esta vacio o no:
    # mostrar_empleado(empleado) if len(empleado.items()) > 0 else print("No se encontro al empleado" )

# empleado_legajo_buscado = 20001

# ordenar_empleados(empleados, "legajo") # -> para usar la busqueda binaria

    # empleado = buscar_empleado_legajo_binaria(empleados, empleado_legajo_buscado)
    # try:
    #     empleado = buscar_empleado_legajo_binaria(empleados, empleado_legajo_buscado)
    #     mostrar_empleado(empleados(empleado))
    # except ValueError as e:
    #     print(e)

empleado = buscar_empleado_legajo_lineal_sin_break(empleados, 20001)
mostrar_empleado(empleado) if len(empleado.items()) > 0 else print("No se encontro al empleado")

# -------------------------- 1 ---------------------------
print("-------------- #1 -------")
#1 mostrar por consola los nombres y sectores de los empleados
# 1a del profe
for el in mapear_nombres_sectores(empleados):
    print(el[0], el[1])
print("-------------------------------")
print("ARRIBA: profe, ABAJO: compañero")
print("-------------------------------")
# 1b de un compañero:
mostrar_empleados_nombre_sector(empleados)

# -------------------------- 2 ---------------------------
print("-------------- #2 -----------------")
#2 pedir un sector y mostrar los empleados de ese sector
sector = input("Ingrese el sector a buscar: ")
empleados_sector = filtrar_empleados_sector(empleados, sector)
mostrar_empleados(empleados_sector)

# -------------------------- 3 ---------------------------
print("-------------- #3 -----------------")
#3 pedir un sector y mostrar el promedio de los sueldos de ese sector
promedio = promedio_sueldo_empleados(empleados_sector)
print(f"Promedio sueldo sector {sector}: ${promedio:.2f}")

# -------------------------- 4 ---------------------------
print()
print("-------------- #4 -----------------")
#4 mostrar el promedio de sueldos de cada uno de los sectores
        # a- Con funciones: mapear_sectores, lista_sin_repetidos -> obtengo todos los sectores sin repetir, es decir filtro la lista -> asi lo veo: print(mapear_sectores(empleados))

sectores = mapear_sectores(empleados) # guardo la lista filtrada

for sector in sectores: # va a hacer cada uno por cada sector
    empleados_sector = filtrar_empleados_sector(empleados, sector)
    promedio = promedio_sueldo_empleados(empleados_sector)
    print(f"Promedio sueldo sector {sector}: ${promedio:.2f}")
    print("------------------------")













