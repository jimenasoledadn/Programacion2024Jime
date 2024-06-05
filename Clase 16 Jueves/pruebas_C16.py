# 3




cadena = "     Hola mundo      "
# strip() --> significa reportar . Si no le paso nada, limpia la cadena y se saca los espacios en blanco qe tenga antes y despues 
    # Si le paso un caracter, se los saca, siempre y cuando esten en las puntas .. 
    # rstring("o") --> saca lo que tenga a la derecha, en este ejemplo la letra 'o'
    # lstring() --> saca lo que tenga y le pase a la izquierda
cadena = cadena.strip()
cadena2 = "Hola Mundo"
cadena3 = cadena2.strip("\n") # para que no haga el \n y se vaya hacia abajo, ya que al apretar enter mas este \n, dejaria un espacio vacio entre este print y el siguiente. Esto es para que no deje una linea intermedia en blanco/vacio
print(cadena)
print(cadena2)
print(cadena3)


