numero = int(input("Ingresa un número (positivo)"))

# PARES

if(numero % 2 == 0):
    print("El número " + str(numero) + " es par")
else:
    print("El número " + str(numero) + " no es par")

# PRIMOS

validador = 0
for num in range(1,numero+1):
     if(numero % num == 0):
        validador += 1
print(validador)
if(validador > 2 or numero == 1):
    print("El número " + str(numero) + " no es primo")
else:
    print("El número " + str(numero) + " es primo")

