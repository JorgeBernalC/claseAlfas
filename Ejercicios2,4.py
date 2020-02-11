"""numeros = [2,3,4,5]

def cuadrado(numero):
    return numero*numero

print(list(map(cuadrado, numeros)))
"""

numeros = [2,3,4,5]
resultado = lambda posicion: posicion * posicion
print(list(map(resultado,numeros)))
