
def menu()->str:
    limpiar_pantalla()
    print(f"{'Menu de Opciones':^50s}") 
    print("1- Saludar")
    print("2- Brindar")
    print("3- Despedir")
    print("4- Salir")

    return input("Ingrese opcion: ")

def saludar():
    print("Hola, que tal...")

def brindar():
    print("Chin chin...")

def despedir():
    print("Chau, nos vemos...")

def pausar():
    import os
    os.system("pause")

def limpiar_pantalla():
    import os
    os.system("cls")

def pedir_confirmacion(mensaje:str)->bool: # msje: con esto le  puedo escribir el msje que quiero mostrar
    rta = input(mensaje).lower()
    return rta == "s"