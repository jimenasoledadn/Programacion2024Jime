import json


mascota = {"id": 1234, "nombre": "Bobby", "edad": 3 , "vacunado": True, "tipo": "perro"}


print(type(mascota))
print(mascota)

print(" -------------------- ")


mascota_json = json.dumps(mascota, indent=4)
 #  Si nosotros tenemos un diccionario, se lo pasamos a dumps y este lo pasa de diccionario a json, que es de tipo string
 #  Le podemos pasarle la sangria que quiero dejarle, ej 4

print(type(mascota_json))
print(mascota_json)

# -------------

# PARA DIFERENCIAR: python muestra con comillas simples los datos de un diccionario !!!!
# Formato string json: SIEMPRE CON COMILLAS DOBLES

# -------------

# ----------- CAMINO INVERSO ---------------

print(" -------------------- ")

mascota2 = json.loads(mascota_json) # para que lo vuelva a convertir en diccionario
print(type(mascota2))
print(mascota2)


