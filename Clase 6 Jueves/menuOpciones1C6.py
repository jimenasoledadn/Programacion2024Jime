



while True:
    print(f"{'Menu de Opciones':^50s}") 
    print("1- Saludar")
    print("2- Brindar")
    print("3- Despedir")
    print("4- Salir")

    opcion = input("Ingrese opcion: ")

    # if opcion == "4":
    #     break

    match opcion:
        case "1":
            print("Hola, que tal...")
        case "2":
            print("Chin chin...")
        case "3":
            print("Chau, nos vemos...")
        case "4":
            break
        


print("Fin del programa")


