def factorial(n:int)->int:
    if n == 0 or n == 1 :
        return 1
    else:
        return n * factorial(n-1)
    
# -------------

print(factorial(1))


# -------------
print("--------")
# OTRA FORMA DE HACER SIN LOS RETURN:

def factorial(n:int)->int:
    fact = None
    if n == 0 or n == 1:
        fact = 1
    else:
        fact = n * factorial(n-1)

    print(fact) # Solo a modo de prueba en esta muestra
    return fact

# --------------

print(factorial(5))