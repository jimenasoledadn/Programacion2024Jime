# archivo: 
#     nombre_archivo.____ -> la extension -> que es el programa que va a abrir este archivo
# es quien va a entender que es lo que hay adentro

# EXTENSION del archivo: determina de que tipo es para que el sistema operativo vea que tipo de programas pueden abrirlo para poder ser usado. Pero se puede abrir con cualquier programa, el problema es que si es de tipo binario, por ejemplo, no va a poder ser "traducido" por un programa que ejecuta texto plano. Otro ejemplo es que si creo un archivo .html de paginas web, me dara la opcion de abrirlo en Chrome o Edge, pero tambien podria elegir un block de notas ya que es un tipo de archivo de texto plano
# Para poder leerse ese archivo tiene que estar cargado en la memoria RAM
# Antes de que se apague la computadora si quiero conservar ese archivo tengo guardarlo en el DISCO RIGIDO




# --------DISCO RIGIDO:
# Es una unidad de almacenamiento
# aca guardamos la info que quiero que quede hasta despues de apagar la computadora
# Siempre van  a permancer en la pc

# -------RAM:
# Son un grupo de transistores abiertos y cerrados (capacitores prendidos o apagados)
# aca solo se guarda mientras la compu este prendida
# Aca cuando se apaga la computadora, los transistores se vacian, se descargan

# -------ARCHIVO: 
# esta en el disco rigido. Cuando se prende la computadora, y si esta tiene iterfaz grafica, al hacerle click o doble click, el sistema operativo (que tienen un programa predeterminado para abrir ese tipo de archivos) utiliza la extension de este archivo para poder abrirlo. El programa que abra este archivo tiene que entender que hay dentro, pueden ser varios programas pero en general siempre hay uno de ellos que es el predeterminado.
# Este archivo que esta en el DR, cuando lo ejecutamos, este archivo se lee y se carga en la memoria RAM,(para poder ejecutarse este tiene que si o si estar cargado en la memoria RAM)
    # Tienen 2 formatos: 
        # Archivos de texto: aca esta guardado el codigo ASCII, la representacion de cada caracter de 0 y 1 (cada caracter ocupa un 8 bitz = 1 byte). Hasta terminar el archivo: EOF -> que quiere decir que hasta ahi llego el archivo, es donde termina.
        # Archivos Binarios: aca en ceros y unos. Aca lo guardo igual que como esta en memoria, si esta en entero, lo guardo como entero; si esta en texto primero se pasa a entero
# Podemos CREAR, ESCRIBIR, y/o LEER un archivo.
    # 1- Abrimos un archivo
    # 2- Usamos el archivo (se lee y escribe)
    # 3- Cerramos el archivo-> Siempre hay que hacerlo ya qe se pueden corromper

# MODOS de un archivo:
    # r: lectura - read -> lo abrimos para leer
    # w: escritura - escribir
    # a: append -> para agregar algo al final del archivo
    # rb: lectura binaria -> para leer escritura binaria
    # wb escritura binaria
    # wa: append binario

    # Por defecto siempre es 'r'

# El archivo se abre con OPEN, el siguiente parametro es el nombre del archivo
