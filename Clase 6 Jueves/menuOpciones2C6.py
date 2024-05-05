import os


def menu()->str:
    os.system("cls")
    print(f"{'Menu de Opciones':^50s}") 
    print("1- Saludar")
    print("2- Brindar")
    print("3- Despedir")
    print("4- Salir")

    return input("Ingrese opcion: ")

# -----------------------------

while True:
    match menu():
        case "1":
            print("Hola, que tal...")
        case "2":
            print("Chin chin...")
        case "3":
            print("Chau, nos vemos...")
        case "4":
            break
    
    os.system("pause")

print("Fin del programa")