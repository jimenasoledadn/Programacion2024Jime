import json
from sort_lambda_c17 import *

with open ("./csv/personas.json", "r", encoding="utf-8") as archivo:
    personas = json.load(archivo) # le paso el archivo que tiene que leer.
    print(archivo.closed) # propiedad booleana para saber si el archivo esta cerrado o abierto


sort_list(personas, compare_persona)




for persona in personas:
    print(persona)

print(" -------------------------------------- ")
print(archivo.closed)

for persona in personas:
    persona["nombre"] = persona["nombre"].upper()

# para guardarlo en otro archivo:

with open ("./csv/personas_mayusculas.json", "w", encoding="utf-8") as archivo:
    json.dump(personas, archivo, indent=4) # si quiero que lo escriba en un archivo, va sin S. Esta lista de personas quiero que lo guardes en formato json en este archivo
