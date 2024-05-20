




# INPUT = SIEMPRE devuelve str. TODO lo que entre por consola es tomado como cadena de caracteres
 # FUNCION INT: es una funcion CONSTRUCTORA de enteros, se lo utiliza en los INPUT para convertir un numero que ingresa por consola en un entero. 
        # Se encarga de convertir TODO en entero

# TRUE: 1 : transistor cerrado
print(int(True))
# FALSE: 0 : transistor abierto
print(int(False))

        # IMPORTANTE!!!! Dar un msje al usuario de que se cometio un error es de principiantes.. Lo que hace INT cuando ocurre un ERROR es lanzar una EXCEPTION, con la palabra reservada RAISE, (una exception es un OBJETO de error, es decir lanza un objeto). Utilizado con METODOS (que son funciones).
# Estos METODOS son formas de comunicarnos con los OBJETOS de AFUERA hacia ADENTRO. Le estamos diciendo a ese objeto que EJECUTE ese metodo
# Los objetos reciben siempre cosas desde afuera, solo hay DOS cosas que pueden LANZAR ellos:
                #    Excepciones: que son objetos de tipo ERROR. Avisan que se llego a una situacion que no se puede realizar como corresponde (ej dividir por cero, no era el dato, etc) No muestra msje por consola!!! Nosotros DEBEMOS manejar ese error.
print("-----")
        # HAY QUE VALIDAR EL TIPO DE DATO que se pide en los parametros:

# Es una instancia: un objeto es una instancia de una clase,
        # Le tengo que pasar un objeto, y una clase. Y me va a decir si pertenece a ese tipo de clase ese objeto o no
x = 5
print(isinstance(x, int)) # x es una variable de tipo int ?
x = 5
print(isinstance(x, float))
x = "Hola"
print(isinstance(x, str))

# Las funciones tienen que ser ROBUSTAS: un codigo es robusto cuando evita errores, no trabaja con datos invalidos
# Los TRY/EXCEPT NO!!!!! se usan en una funcion. El usuario NO tiene que ver mensajitos del programador por pantalla. Los T/E se usan cuando se USA la funcion, y los msjes se muestran 

# EJEMPLO: si a la funcion dividir le tiraste algo que no puede hacer, la funcion protesta, y el que deberia hacer un T/E es AFUERA de la funcion
# Los mensajes en la CONSOLA los pone solamente el programa principal!!! Si el programa principal que va llamando a las funciones y estas/esta funciones no pueden resolver el problema, el programa principal NO MUESTRA MSJE POR PANTALLA. Solo AVISA que ocurrio un error. El programa principal es el que CAPTURA ESE error, y es el que decide QUé es lo que va a mostrar por pantalla. Los PRINT Siempre van desde el programa principal (salvo que sea una funcion para imprimir algo), las funciones NO SE COMUNICAN con el usuario a traves de la pantalla


# -----------------------------

# NO haria falta un else, ya que el RAISE es como un break, una vez que se ejecuta se sale de la funcion. Es decir es la ultima linea que se va a ejecutar en esta funcion, todo lo que este despues NUNCA se va a ejecutar, en cambio si no entra en este if, va a pasar directamente al codigo de la funcion

# -------------------

# def contar_en_lista(lista:list, target:any)->int: 
        # ANY es el tipo de dato por defecto, puede ser de cualquier tipo. No va a tirar ERROR

# ------------

#  Para el sorteador: 
# 1 ) copio de la lista de presentes
# 2 ) se lo paso a chat gpt y le pidio que se lo devuelva con los       apellidos entre comillas, separados por coma
# 3 ) armo un se...  x = set[ aca copio todos los nombres que le armo el chat gpt]
#         SET: el constructor de set espera un iterable, asi que le paso una lista SIN repetidos
# 4 ) Arma una lista y le pasa el SET que se armo, para que no tenga repetidos    apellidos = list(x)
#         print(apellidos)
#         print(x)

# ------------------------------------

        # PARAMETROS POR DEFECTO:
# def ordenar_lista(lista:list, ascendente:bool = True)->None: # Significa en este caso que el parametro qe le paso, por defecto va a ser ASCENDENTE -> TRUE!
# Entonces cuando llamo a la funcion:
        # ordenar_lista([nombre_de_la_lista]) -> ya lo toma como TRUE, entonces lo va a ordenar de forma ascendete. O escrito directamente --> ordenar_lista([nombre_de_la_lista], True)
        # Y si quiero que los ordene de forma Descendente, tengo que aclararlo como False : ordenar_lista([nombre_de_la_lista], False)

