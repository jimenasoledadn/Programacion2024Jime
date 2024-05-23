


alumno = {"legajo":20000,
          "nombre": "Juan",
          "genero": "m",
          "nota_p1": 6,
          "nota_p2": 7,
          "promedio": 6.5}

print(alumno)
print(id(alumno))

print(alumno["legajo"]) # pongo el nombre de la keys

alumno["localidad"] = "Avellaneda"
alumno["legajo"] = 30000

y = "localidad"
print(alumno[y])
x = "nombre"
print(alumno[x])
print(alumno)

print(id(alumno))

print(alumno.get("localidad")) # retorna el valor de la key si esta en el diccionario
print(alumno["localidad"]) # --> aca accedo a traves de [] pero tambien se puede con .get

print(alumno.get("email")) # EN CAMBIO Si NO existe me tira None
# y a parte me permite si le paso como segundo parametro:
print(alumno.get("email", "no existe el parametro")) # Es como si tuviera un if adentro del metodo
print(alumno["email"]) # Si no existe me tira error de key

print(alumno.keys()) # es un metodo, es una forma de verlo como una lista pero NO lo es! 

# ASI me dice que NO es un iterable... PERO...
for key in alumno.keys:
    print(key)
    
    # puedo transformalo en una lista:
claves = list(alumno.keys())
print(claves)

# ... si lo transformo en una lista: lo puedo recorrer: 
for key in alumno.keys():
    print(key)

# tambien tenemos alumnos.values:
for key in alumno.values():
    print(key)

# pop remueve el campo que elijo

# popitem REMUEve un campo al azar