
# modos:
    # "w" --> Si no existe, lo crea.
                # El problema es que si el archivo ya existe, al abrirlo SE BORRA TODO, aunque no se escriba nada
    # "x" --> para CREAR un archivo, sin que lo abra ni lo escriba. Si ya existe, NO lo crea
    # "a" --> con esto podemos modificar el archivo si es que existe, si no existe NO lo crea

with open("./archivos/mi_archivo.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola mundo")

# EL PROBLEMA: de abrir/leer/crear archivos de esta forma --> ./archivos/... Si yo llegara a querer abrir SOLO la carpeta archivos en el VScode, y desde ahi empezara a trabajar, no encontraria estos archivos nuevos creados de esta forma. Ya que la buscaria en un directorio raiz que ahora "no esta", esta abierto directamente desde mi_archivo (en este ejemplo). Va a buscar un directorio llamado archivos.






