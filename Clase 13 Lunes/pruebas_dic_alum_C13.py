from random import choice




print(type({})) # Las llaves directamente son un diccionario vacio
print("-----------")

valores = [[1,5,32,56], ['a','b','c'], ["Python", [{"clave_1":True, "clave_2":"hola", "clave_3":1234}, "chau"], 200, 300]]

print(type(valores))
print(len(valores))
print("-----------")
print(valores[2]) # NUNCA hay que usar este, xq en teoria no conocemos el valor o indice donde esta
print(len(valores) - 1) # La mejor forma!!!! Por si se llega a actualizar algun dato, esto seguiria sirviendo
print(valores[-1]) # Esto en algunos lenguajes no funciona
print("-----------")
print(valores[1])
print(valores[1][1])
print("-----------")
print(valores[2])
print(valores[2][0])
print(valores[2][1][1])
print(valores[2][1][0])
print(valores[2][1][0]["clave_2"])

print("------- Choice: -----")

for _ in range(20):
    print(choice(['m', 'f']))