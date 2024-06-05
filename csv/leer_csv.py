def get_path_actual(nombre_archivo):
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

with open(get_path_actual("personas.csv"), "r", encoding="utf-8") as archivo:
    lista = []
    encabezado = archivo.readline().strip("\n").split(",")
    # me trae las lineas que estan a continuacion
    for linea in archivo.readlines():
        persona = {}
        linea = linea.strip("\n").split(",")
        id, nombre, apellido, genero, edad, peso = linea # esto es un desempaquetado de Lista
        
        persona["id"] = int(id)
        persona["nombre"] = nombre
        persona["apellido"] = apellido
        persona["genero"] = genero
        persona["edad"] = int(edad)
        persona["peso"] = float(peso)
        lista.append(persona)

for persona in lista: # POR QUE ME APARECEN MUCHOS DEL ID 20 !!!!!! PREGUNTAR
    print(persona)


for i in range(len(lista)):
    lista[i]["nombre"] = lista[i]["nombre"].upper()
    print(persona)

print(".......")
for persona in lista:
    print(persona)
        


with open(get_path_actual("personas_mayusculas.csv"), "w", encoding="utf-8") as archivo:
    # keys = list(lista[0].keys()) # 
    # print(keys)

    # encabezado = ",".join(keys) + "\n" # join : juntar-- este metodo recibe la lista keys para juntarlos. y asi hacer el camino inverso. Le sumo la \n

    # print(encabezado)
    #  O TODO JUNTO:
    encabezado = ",".join(list(lista[0].keys())) + "\n"
    archivo.write(encabezado)
    for persona in lista: # persona es un diccionario, y a cada persona quiero extraerle los values
        values = list(persona.values())
        l = []
        for value in values:
            
            if isinstance(value, int):
                l.append(str(value))
            elif isinstance(value, float):
                l.append(str(value))
            else:
                l.append(value)
            
        linea = ",".join(l)  + "\n"
        archivo.write(linea)


# funcion: leer archivo, pasarle el nombre del archivo csv y devuelva la lista --> lo levanto 
# funcion: guardar en archivo csv, pasandole la lista y el nombre del archivo --> lo guardo


