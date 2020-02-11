numero = int(input("Ingresa un número> "))
numero2 = int(input("Ingresa un número> "))
numero3 = int(input("Ingresa un número> "))
resultado = lambda numero, numero2, numero3: numero + numero2 + numero3

"""
def funcion(numero):
    return (numero + 10) * 2
"""

print(resultado(numero, numero2, numero3))