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

    # 2a)

while True:
    edad = input("Ingrese edad mayor o igual a 18: ")
    if(edad.isdigit()): # un valor invalido es que NO tenga digitos
        edad = int(edad)
        if edad < 18:
            print("Edad invalida")
        else:
            break
    else:
        print("Eso no es un numero")
print(edad)

    # 3a)
while True:
    try: # NO hace falta validar porque asume en el try que salio todo bien, sino ira al except
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
    except ValueError:
        print("Eso no es un numero")
    except:
        print("Edad invalida") # Puedo hacerlo asi, o directamente dejarlo arriba en el raise
    # Es como un MATCH agarrador de excepciones 
print(edad)

        # 2b)
while True:
    aux = input("Ingrese edad mayor o igual a 18: ") # O en vez de aux, llamar a la variable ´entrada´ (la entrada del usuario)
    if(aux.isdigit()):
        edad = int(aux)
        if edad < 18:
            print("Edad invalida")
        else:
            break
    else:
        print("Eso no es un numero")
print(edad)