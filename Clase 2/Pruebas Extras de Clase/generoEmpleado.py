

#GENERO:

    # 1)

# genero = input("Ingrese genero del empleado: ")
# # mientras el genero sea invalido ( o sea diferente de masculino y diferente de femenino) voy a informar que el dato es invalido y lo voy a volver a pedir
# while genero != "Masculino" and genero != "Femenino": # o --> while not (genero == "Masculino" or genero == "Femenino") --> QUIERO entrar al while cuando no sea valida la condicion 
#     genero = input("Genero invalido. Ingrese el genero del empleado: ")
# print(genero)

    # 2)

# def generoValido(genero):
#     return genero == "masculino" or genero == "femenino"

# genero = input("Ingrese genero del empleado: ").lower()
# OTRA FORMA:  mientras el genero NO sea valido (pongo lo valido en la condicion del while)
# while not generoValido(genero):
#     genero = input("Genero invalido. Ingrese el genero del empleado: ").lower()
# print(genero)

# FORMA 1) Si funciona!!!

# genero = input("Ingrese genero empleado: ")
# while not (genero == "Masculino" or genero == "Femenino"):
#     genero = input("Genero invalido, Ingrese genero empleado: ")
# print(genero)  

def generoValido(genero):
    return genero == "masculino" or genero == "femenino"

genero = input("ingrese genero empleado: ").lower() 
while not generoValido(genero):
    genero = input("Genero invalido, Ingrese genero valido: ").lower()
print(genero)