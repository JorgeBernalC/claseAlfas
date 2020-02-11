# """
# ESTRUCTURA DE UNA FUNCION EN PYTHON
# def nombre_de_la_funcion(argumentos):
#     operacion
#     operacion 2
#     return operacion3 /// print(operacion3)
# """

# def saludo(nombre):
#     return "Hola " + nombre + "!!"

# nombre = input("Ingresa tu nombre ")
# print(saludo(nombre))

# #def saludo(nombre):
# #     print("Hola " + nombre + "!!")
# #     return None

# # nombre = input("Ingresa tu nombre ")
# # saludo(nombre)
# numero1 = int(input("Ingresa un numero> "))
# numero2 = int(input("Ingresa otro numero> "))

# def suma(numero1, numero2):
#     return numero1 + numero2

# print(suma(numero1, numero2))

# def resta(numero1, numero2):
#     return numero1 - numero2

# print(resta(numero1, numero2))

"""def posicional(*args):
    for arg in args:
        print(arg)
posicional(1, "Argumento posicional", [1,2,3,4,5], "Args pos #4")

# def posicional(*args):
#     for arg in args:
#         print(arg)
#     return None
# posicional(1, "Argumento posicional", [1,2,3,4,5])

def nombre(**kwargs):
    for argumento in kwargs:
        print(str(argumento) + " = " + str(kwargs[argumento]))
    return None

nombre(a=1, b="Hola", c="Adios", d=4.2)"""

# Pasar varios argumentos con o sin nombre
# Para los argumentos sin nombre, debera imprimir su valor
# Para los argumentos con nombre, debera imprimir el nombre y su valor

# def combinacional(*args, **kwargs):
#     for args in args:
#         print(str(arg))
#     for args in kwargs:
#         print(str(arg))

# combinacional(valor1=2, valor2=4, nombre="Juan", apellido="Pedro", 15, 26, "Luis", "Carlos")

def combinacional(*args, **kwargs):
    suma = 0
    for arg in args:
        suma += arg
    print("Suma = " + str(suma))

    for kwarg in kwargs:
        print(str(kwarg) + " = " + str(kwargs[kwarg]))

combinacional(2, 4, 6, a="A", b="B", c="C")