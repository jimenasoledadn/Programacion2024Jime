# Ejercicio Nivelación

# Una reconocida productora de contenidos audiovisuales está en busca de nuevas ideas
# para su próximo proyecto, que promete cautivar al público.
# Las posibles temáticas para explorar son las siguientes:
# • Comedia
# • Ciencia ficción
# • Drama
# Para ello, la empresa ha decidido realizar una encuesta entre sus empleados para
# recopilar información valiosa. Los datos para recopilar por cada empleado son los
# siguientes:
# A) Información a ingresar por cada empleado encuestado:
# • Nombre del empleado
# • Edad (debe ser mayor o igual a 18)
# • Género (Masculino - Femenino)
# • Temática de interés (Comedia, Ciencia ficción, Drama)
# B) Se deben cargar 10 encuestas a través de la terminal.
# C) Se requiere determinar:
# • La cantidad de empleados de género masculino que votaron por Ciencia ficción o
# Drama, cuya edad esté entre 25 y 50 años, inclusive.
# • El porcentaje de empleados que no votaron por Comedia, siempre y cuando su
# género no sea Femenino o su edad esté comprendida entre 30 y 40 años.
# • El nombre y la temática de interés votada por el empleado masculino de mayor
# edad.

CANT_ENCUENTAS = 2
contador_punto_1 = 0
contador_punto_2 = 0

# nombre:
for i in range(CANT_ENCUENTAS):
# NOMBRE:
    nombre = input("Ingrese nombre del empleado: ")
    while not nombre.isalpha():
        nombre = input("Nombre invalido. Ingrese bien el nombre del empleado: ")


# Edad:
    while True:
        try: # NO hace falta validar porque asume en el try que salio todo bien, sino ira al except
            edad = int(input("Ingrese edad mayor o igual a 18: "))
            if edad <= 18:
                print("EDAD INVALIDA)")
            else:
                break # para sacarnos del while si el dato es valido
        except:
            print("Eso no es un numero")        


    # Genero:
    def generoValido(genero):
        return genero == "masculino" or genero == "femenino"

    genero = input("ingrese genero empleado: ").lower() 
    while not generoValido(genero):
        genero = input("Genero invalido, Ingrese genero valido: ").lower()
    

    # Tematica: 
    def tematicaValida(tematica):
        return tematica == "ciencia" or tematica == "comedia" or tematica == "drama"

    tematica = input("Ingrese la tematica del empleado: ").lower()
    # mientras el genero NO sea valido (pongo lo valido en la condicion del while)
    while not tematicaValida(tematica):
        tematica = input("Tematica invalida. Ingrese la tematica del empleado: ").lower()

    # Para cumplir el punto 1)
    if genero == "masculino" and \
        (tematica == "ciencia" or tematica == "drama") and \
            (edad >= 25 and edad <= 50): # siempre en minuscula porqe vamos a validarlos en minusculas 
        contador_punto_1 += 1

    # Para cumplir el punto 2)
    if (tematica != "comedia") and \
        (genero == "masculino" or (edad >= 30 and edad <= 40)) : # que no haya votado por comedia (*)
        contador_punto_2 += 1
    #(*) tambien se puede hacer para el punto 2) :
    # if not (tematica == "drama" or tematica == "ciencia") -> 
    #     pass



print("1) ", contador_punto_1)

porcentaje_punto_2 = contador_punto_2 * 100 / CANT_ENCUENTAS
        
print("Respuesta punto 2: ", porcentaje_punto_2
      )

# despues del for