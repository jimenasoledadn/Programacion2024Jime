#TEMATICA

# tematica = input("Ingrese tematica: ").lower()

# while not (tematica == "ciencia" or tematica == "comedia" or tematica == "drama"): # mientras tematica no sea nada de esto que esta entre parentesis, va a entrar al while
#     tematica = input("Tematica invalida. Ingrese tematica: ").lower()
# print(tematica)


# def tematicaValida(tematica):
#     esValido =  (tematica == "ciencia" or tematica == "comedia" or  #       tematica == "drama")
#     return esValido

def tematicaValida(tematica):
    return tematica == "ciencia" or tematica == "comedia" or tematica == "drama"

tematica = input("Ingrese la tematica del empleado: ").lower()
# mientras el genero NO sea valido (pongo lo valido en la condicion del while)
while not tematicaValida(tematica):
    tematica = input("Tematica invalida. Ingrese la tematica del empleado: ").lower()
print(tematica)