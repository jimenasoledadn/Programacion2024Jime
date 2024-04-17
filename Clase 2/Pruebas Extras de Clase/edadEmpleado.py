# EDAD:

    # try: # trata de convertir la entrada en entero 
    #     edad = int(input("Ingrese edad mayor o igual a 18: "))
    
    # except: # Pero si encuentra un error, es capturado por el except. Y este puede resolverlo o no. 
    #     print("Eso no es un numero")

    # print(edad) # Se va a mostrar siempre, entre o no en el except
    # 1)

    # while True:
    #     try:
    #         edad = int(input("Ingrese edad mayor a 18: "))
    #         if edad < 18:
    #             print("EDAD INVALIDA)")
    #         else:
    #             break # para sacarnos del while si el dato es valido
    #     except:
    #         print("Eso no es un numero")

    # print(edad)

    # 2)
edad = input("Ingrese edad mayor o igual a 18: ")
if(edad.isdigit()):
    edad = int(edad)
    if edad < 18:
        print("Edad invalida")
    else:
        break
else:
    print("Eso no es un numero")

    # 3a)
    while True:
        try:
            edad = int(input("Ingrese edad mayor a 18: "))
            if edad < 18:
                print("EDAD INVALIDA)")
            else:
                break # para sacarnos del while si el dato es valido
        except:
            print("Eso no es un numero")
            
    print(edad)

    # 3b)
    while True:
        try:
            edad = int(input("Ingrese edad mayor a 18: "))
            if edad < 18:
                raise Exception()  # esuna excepcion generica o ("Edad menor a 18") 
            else:
                break # para sacarnos del while si el dato es valido
        except:
            print("Eso no es un numero")
        except:
            print("Edad invalida") # Puedo hacerlo asi, o directamente dejarlo arriba en el raise
        # Es como un MATCH agarrador de excepciones 
    print(edad)

    # 3c)
    aux = input("Ingrese edad mayor o igual a 18: ")
    if(aux.isdigit()):
        edad = int(aux)
        if edad < 18:
            print("Edad invalida")
        else:
            break
    else:
        print("Eso no es un numero")