

with open("archivos/mi_archivo.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo.readlines(): 
        dato = linea.strip("\n")
        print(dato)