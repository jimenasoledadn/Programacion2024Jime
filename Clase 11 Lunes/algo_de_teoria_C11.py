# Ejemplo si llamo a un archivo, puedo renombrar en mi programa a alguna de las listas que se encuentren dentro de ese archivo:

# from data_warehouse_C11 import nombres as names # as names, estoy renombrando la lista nombres, por names.
# from funciones_paralelas_C11 import *
from prueba_Jime import * 
# -----
# Renombro la lista, ya que aca tengo una variable que guarda la direccion de memoria de una lista, CON EL MISMO NOMBRE. Entonces para que esta ultima NO pise a la otra, renombro la que traigo de otro archivo

nombres = [] 

print(nombres)
print("----ARRIBA: nombres ---- ABAJO: names-----")
print(nombres2)

# --------------------------------
    # def cargar lista nombres(): --> lista = nombres[:cantidad]
# Para mostrar como la sublista pisa a la lista "original". Pero una vez que termina la funcion, vuelve a la direccion de memoria originaria. Esto explica que no se debe de asignar con una igual.
            # print()
            # print(id(nombres))
            # cargar_lista_nombres(nombres, names, 10)
            # print("Fuera de la lista ", id(nombres), nombres)

# ----------------------------------

