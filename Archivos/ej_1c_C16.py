archivo = open("./archivos/ejemplo1.txt", "r", encoding="utf-8") 

# PARA PODER LEER UN ARCHIVO:

with open("./archivos/ejemplo1.txt", "r", encoding="utf-8") as archivo:
    dato = " "
    # Si no se conoce la cantidad de lineas , UNA FORMA:
    # while datos != "":
    #     datos = archivo.readline().strip("\n") #
    #     print(datos)
    # OTRA FORMA:
    for linea in archivo.readlines(): # readlines me devuelve una lista de todas las lineas qe tiene el archivo, un iterable para poder recorrer
        dato = linea.strip("\n")
        print(dato)



