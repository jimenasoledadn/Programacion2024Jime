

# Pedir al usuario 5 numeros y mostrarlos por consola utilizando una lista
CANT = 5
lista = []

for i in range(CANT): # Como la variable i NO SE USA, podemos poner en ese lugar (en el range), un _ (guion bajo): for _ in range(CANT):
    numero = int(input("Ingrese un numero: "))
    lista.append(numero)

print(lista[:])
        # En todas las formas i puede obtener otro nombre
# UNA FORMA:
for i in range(CANT):
    print(lista[i], end=" ")             # print(lista[i])
print("\n------------")
# OTRA FORMA
for i in lista:
    print(i, end=" ")                    # print(i)
print("\n------------")
# OTRA FORMA:
for i in range(len(lista)):
    print(lista[i], end=" ")             # print(lista[i])


