


datos = [43, 5, 78, 32, 12, 43, 76, 39]


print(datos[len(datos) - 1]) # me va a imprimir el elemento 39
print(datos[-1]) # Otra forma para que me imprima el ultimo numero
print(datos[-7]) # va a imprimir el primer numero asi7

# Puedo armar subListas:
print(datos) # ACA me muestra la lista completa
print(datos[1:6]) # desde donde quiero que arranque hasta el indice 6, pero este indice NO ESTA INCLUIDO, el de la izquierda o sea el indice 1 si!!! 
print(datos[2:]) # Si dejo ese espacio vacio, quiere decir desde el indice 2 hasta EL FINAL
print(datos[:7]) # vacio el primer espacio es como si pusiera de indice 0, o sea desde el principio hasta el indice 7 que NO SE VA A MOSTRAR
print(datos[:]) # quiero que me muestre TODA la lista

a = 3
b = 8
print(datos[a:b])