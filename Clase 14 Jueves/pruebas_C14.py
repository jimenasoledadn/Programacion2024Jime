
from funciones_empleados_C14 import *


lista = [1,5,6,8,9,12,15,19,45,65,87,92]
numero_a_buscar = 23

# def busqueda_binaria(lista: list, target: int):
#     inf = 0
#     sup = len(lista) - 1 
#     while inf <= sup:
#         medio = (inf + sup) // 2
#         if target == lista[medio]:
#             return medio
#         elif target > lista[medio]:
#             inf = medio + 1
#         else:
#             sup = medio - 1 
#     raise ValueError(f"{target} in not in list")

print(busqueda_binaria(lista,numero_a_buscar))