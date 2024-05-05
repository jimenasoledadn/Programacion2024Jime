


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


# -----------------------------

while True:
    match menu():
        case "1":
            saludar()
        case "2":
            brindar()
        case "3":
            despedir()
        case "4":
            break
    
    pausar()

print("Fin del programa")