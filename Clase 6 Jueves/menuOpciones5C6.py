
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

flag_saludo = False
flag_brindis = False

while True:
    match menu():
        case "1":
            saludar()
            flag_saludo = True
        case "2":
            if flag_saludo:
                brindar()
                flag_brindis = True
            else:
                print("Debes saludar antes de brindar...")
        case "3":
            if flag_brindis: 
                despedir()
                flag_saludo = False
                flag_brindis = False # Estos dos, para que se vuelva a bloquear el programa
            elif flag_saludo:
                print("Brindemos antes de despedirnos ")
            else:
                print("Primero debemos saludarnos y brindar antes de despedirnos")
        case "4":
            break
    
    pausar()

print("Fin del programa")


