"""
Ejercicio 4 - Lambda
Escribe una funcion que pida al usuario numero1, numero2 y numero3.
Al numero 3 lo elevara la cuadrado y luego, sera sumado al numero1 y numero2
"""
numero1 = int(input("Ingresa un numero> "))
numero2 = int(input("Ingresa un numero> "))
numero3 = int(input("Ingresa un numero> "))

resultado = lambda numero1, numero2, numero3: (numero3 * numero3) + numero2 + numero1

print(resultado(numero1, numero2, numero3))