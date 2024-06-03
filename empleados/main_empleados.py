from funciones_empleados import *


TAM = 5
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
sector = "Sistemas" #input("Ingrese el sector a buscar: ")
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

# -------------------------- 5 ---------------------------
print()
print("-------------- #5 -----------------")
#5 mostrar el empleado que mas gana y a que sector pertenece

mapeo = mapear_empleados(lambda emp: (emp["legajo"], emp["sueldo"], emp["sector"]), empleados) # me devuelve una tupla con esos campos








# ----------- FUNCION LAMBDA -----------

print(" --- Con funcion: --- ")

def filtrar_femenino(emp:dict)->bool:
    return emp["genero"] == "f"
def filtrar_sistemas(emp:dict)->bool:
    return emp["sector"] == "Sistemas"

empleados_filtrados = filter_empleados(filtrar_femenino, empleados)
mostrar_empleados(empleados_filtrados)

empleados_filtrados = filter_empleados(filtrar_sistemas, empleados)
mostrar_empleados(empleados_filtrados)


print(" --- Con LAMBDA: --- ")

empleados_filtrados = filter_empleados(lambda emp : emp["genero"] == "m", empleados)
mostrar_empleados(empleados_filtrados)
empleados_filtrados = filter_empleados(lambda emp : emp["provincia"] == "Mendoza" and emp["genero"] == "f", empleados)
mostrar_empleados(empleados_filtrados)

# -------------------------------------------------------------
print("--Mapeadora--")

def email_empleado(empleado:dict)->str: # es EMPLEADO, porque va a llamar a UN solo empleado por vez para sacar lo que se necesita
    return empleado["email"] # me devuelve el email del empleado

def edad_empleado(empleado:dict)->str:
    return empleado["edad"]

# -----------------
print("--Con funcion: --")

emails = mapear_empleados(email_empleado, empleados)

for email in emails:
    print(email)    

print("--Con LAMBDA: --")

datos = mapear_empleados(lambda emp: emp["legajo"], empleados)

for dato in datos:
    print(dato)

# ------------

mostrar_empleados(empleados)

# Me esta devolviendo una lista nueva
def aumentar_sueldo(empleado:dict)->None:
    # empleado["sueldo"] = empleado["sueldo"] + empleado["sueldo"] * 10/100
    empleado["sueldo"] *= 1.1
    # return empleado
    
print("Aumento de sueldo: ")

        #por eso lo guardo en una lista nueva, porque modifica la original
        #  Para usar esta forma: tengo que modificar la funcion aumentar_sueldo -> tiene que retornar un diccionario de un empleado: -> dict: y abajo return empleado:
                # def aumentar_sueldo(empleado:dict)->dict:
                    # empleado["sueldo"] = empleado["sueldo"] + empleado["sueldo"] * 10/100 # O asi: empleado["sueldo"] *= 1.1
                        # return empleado
                # empleados_nuevo_sueldo = mapear_empleados(aumentar_sueldo, empleados)
                # mostrar_empleados(empleados_nuevo_sueldo)
        # NO NECESITO DEVOLVER LA LISTA EN LAS FUNCIONES PARA MODIFICARLAS !!!!

# ----------- EACH --------
print(" --------------- ")
each_empleado(aumentar_sueldo, empleados)
mostrar_empleados(empleados)

# --------------------
print(" ---- ")

ordenar_empleados_lambda(lambda emp1, emp2: emp1["apellido"] < emp2["apellido"], empleados) # apellidos de la 'z' a la 'a':
mostrar_empleados(empleados)

print(" ---- ")

ordenar_empleados_lambda(lambda emp1, emp2: len(emp1["apellido"]) < len(emp2["apellido"]), empleados) # apellido del mas largo al mas corto: 
mostrar_empleados(empleados)
print(" ---- ")

ordenar_lista(lambda emp1, emp2: len(emp1["nombre"]) < len(emp2["nombre"]), empleados)
mostrar_empleados(empleados)


# --------------------











