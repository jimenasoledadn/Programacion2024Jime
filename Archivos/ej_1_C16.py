


#open("ejemplo1.txt") # que le ponga la extension, es solo para que se abra con un tipo de programa en particular
    # Me va a tirar una excepction si el archivo NO exite
    # El directorio raiz es Programacion2024Jime, entonces si esta dentro de otra carpeta adentro de esta carpeta raiz, TAMPOCO va a encontrarla: Tengo que hacer lo siguiente

open("./Archivos/ejemplo1.txt")
    # el ./ --> quiere decir anda al directorio raiz o directorio actual del proyecto
    # archivos/ --> es que vaya a la carpeta archivos
    # / nombre del archivo
    # / --> Con la barra estamos habland de un directorio  

    # Con este OPEN le estoy diciendo a python que vaya a esa direccion del disco rigido y cargue ese archivo en memoria RAM

# Cuando no se encuentra como, se llama PATH: que es el camino que hay que seguir para encontrar un archivo

# Creo un objeto de tipo File / archivo
archivo = open("./archivos/ejemplo1.txt", "r", encoding="utf-8") 
    # pongo 'r' aunque por defecto ya se ponga solo, pero para que a modo descriptivo quede mas legible
    # tercer parametro: encoding= es decir como esta codeado este archivo. Siempre vamos a poner UTF-8 --> es parecido al codigo ASCII pero con la parte extendida del codigo ascii
print(type(archivo))

# 1- abro el archivo
# 2- lo guardo en una variable
# 3- le doy el uso que quiero
# 4- lo cierro con el metodo CLOSE

# Para leer el archivo:
datos = archivo.read()

archivo.close()

print(datos)
print(type(datos))

