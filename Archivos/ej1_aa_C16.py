import os
import struct



with open("./archivos/mi_archivo.txt", "rb") as archivo:
    dato = archivo.read(4)
    numero = struct.unpack("i", dato)[0]


print(numero)