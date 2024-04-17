

#GENERO:

    # 1)

genero = input("Ingrese genero del empleado: ")
# mientras el genero sea invalido
while genero != "Masculino" and genero != "Femenino": # while not (genero == "Masculino" or genero == "Femenino")
    genero = input("Genero invalido. Ingrese el genero del empleado: ")
print(genero)

    # 2)

def generoValido(genero):
    return genero == "Masculino" or genero == "Femenino"

genero = input("Ingrese genero del empleado: ").lower()
# mientras el genero sea invalido
while not generoValido(genero):
    genero = input("Genero invalido. Ingrese el genero del empleado: ").lower()
print(genero)