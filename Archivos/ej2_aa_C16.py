import os 
import struct

#1
# path = os.getcwd() # get current working directory
# path = os.path.join(path, "archivos/mi_archivo.txt")

# ------
# 2 Asi es la forma de conseguir la forma de saber el directorio actual en que se encuentra el archivo, con su directorio raiz (programacionJime2024) y en el que esta guardado directamente (archivos), y luego puedo poner el nombre del archivo qe quiero leer o escribir. 
directorio_actual = os.path.dirname(__file__)
path = os.path.join(directorio_actual, "archivos/mi_archivo.txt") # Concateno el directorio en donde estoy parado con el nombre del archivo

print(directorio_actual) # Nos dice donde esta el archivo de donde se esta ejecutando el archivo.
# -----

#1
# print(path)
# numero = 40

# with open(path, "wb") as archivo:
#     archivo.write(struct.pack("i", numero))