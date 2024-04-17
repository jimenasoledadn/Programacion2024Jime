#TEMATICA

tematica = input("Ingrese tematica: ").lower()

while not (tematica == "ciencia" or tematica == "comedia" or tematica == "drama"): # mientras tematica no sea nada de esto que esta entre parentesis, va a entrar al while
    tematica = input("Tematica invalida. Ingrese tematica: ").lower()
print(tematica)