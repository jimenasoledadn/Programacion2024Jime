
CANT_ENCUENTAS = 2



for i in range(CANT_ENCUENTAS):
# NOMBRE:
    nombre = input("Ingrese nombre del empleado: ")
    while not nombre.isalpha():
        nombre = input("Nombre invalido. Ingrese bien el nombre del empleado: ")
    print(nombre)

