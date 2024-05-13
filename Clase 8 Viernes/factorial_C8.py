
def factorial(n:int)->int:
    resultado = 1
    for i in range(1, n+1): # range(1, n+1) => pongo 1 xq el range arranca en 0 por default; y n+1 => xq siempre termina en el numero anterior al que indico (ejemplo si pongo 7 va a terminar en el 6), y yo quiero que tambien se utilice el numero que va a ingresar el usuario, por ello (n+1)
        resultado = resultado * i
    return resultado

# -------------------------------

print(factorial(0))
print("-----")
for numero in range(5):
    print(factorial(numero), end=" ")