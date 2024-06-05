import os


path = os.getcwd() # gert current working directory 
            # Traeme el directorio actual de trabajo
path = os.path.join(path, "archivos/mi_archivo.txt") # sirve para concatenar lo que guarde en el path junto con lo que quiero que cree

# print(path) # aca me va a aparecer el directorio completo

numero = 30
otro_numero = 15
with open(path, "w", encoding="utf-8") as archivo:
    archivo.write("Hola mundo\n") # el write NO tiene \n .. escribe todo seguido, se desplaza
    archivo.write("Hola mundo\n") # para que vaya hacia abajo le tengo que poner el \n
    archivo.write("Hola mundo\n")
    archivo.write(str(numero)+"\n") # tengo que convertirlo en string
    archivo.write(f"{otro_numero}")


    # Esto lo puedo leer desde otro archivo
# with open(path, "r", encoding="utf-8") as archivo:
#     for linea in archivo.readlines(): 
#         dato = linea.strip("\n")
#         print(dato)