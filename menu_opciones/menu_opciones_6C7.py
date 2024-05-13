from saludosC7 import *

# -----------------------------

flag_saludo = False
flag_brindis = False

seguir = "s"

while seguir == "s":
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
            if(pedir_confirmacion("Confirma salida?: s/n ")):
                seguir = "n"
            continue # para que se saltee lo restante, y vuelva a la siguiente iteracion. Aca ocasionara que salga directamente despues de confirma con un 's'
    
    pausar()

print("Fin del programa")