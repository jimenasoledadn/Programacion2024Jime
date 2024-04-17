CANT_ENCUENTAS = 2



for i in range(CANT_ENCUENTAS):
# NOMBRE:
    nombre = input("Ingrese nombre del empleado: ")
    while not nombre.isalpha():
        nombre = input("Nombre invalido. Ingrese bien el nombre del empleado: ")
    print(nombre)

# EDAD:s

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


#GENERO:

    # 2)
def generoValido(genero):
    return genero == "Masculino" or genero == "Femenino"

genero = input("Ingrese genero del empleado: ").lower()
# mientras el genero sea invalido
while not generoValido(genero):
    genero = input("Genero invalido. Ingrese el genero del empleado: ").lower()
print(genero)

#TEMATICA

tematica = input("Ingrese tematica: ").lower()

while not (tematica == "ciencia" or tematica == "comedia" or tematica == "drama"): # mientras tematica no sea nada de esto que esta entre parentesis, va a entrar al while
    tematica = input("Tematica invalida. Ingrese tematica: ").lower()
print(tematica)