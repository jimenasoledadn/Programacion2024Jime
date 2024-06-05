archivo = open("./archivos/ejemplo1.txt", "r", encoding="utf-8") 


with open("./archivos/ejemplo1.txt", "r", encoding="utf-8") as archivo: # con as le estoy asignando un nuevo nombre a la apertura del archivo
    # Mientras este adentro del bloque, quiere decir que estoy con el archivo abierto y estoy trabajando con el: Abro un bloque con los dos puntos
    # datos = archivo.read()
    # print(datos)
    # print("----")
    datos = archivo.readline() # Leo la primer linea
    print(datos, end="")
    print("----")
    datos = archivo.readline().strip("\n") #
    print(datos)
    print("----")


# print("Fin") 
# Aca NO hace falta cerrar el archivo. Ya que se cierra automaticamente. Puede usarse de la forma como en el ej_1_C16