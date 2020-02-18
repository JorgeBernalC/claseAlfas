'''def IVA(cantidad):
    resultado = cantidad + cantidad*0.16
    print("Resultado>")
    print(resultado)
cantidad = float(input("Escribe una cantidad> "))
IVA(cantidad)
'''
# def Mayor(num1, num2, num3):
#     mayor = 0
#     if(mayor <= num1):
#         mayor = num1
#     if(mayor <= num2):
#         mayor = num2
#     if(mayor <= num3):
#         mayor = num3
#     print("El número más grande es>")
#     print(mayor)
# num1 = int(input("Ingresa el primer numero> "))
# num2 = int(input("Ingresa el segundo numero> "))
# num3 = int(input("Ingresa el tercer numero> "))
# Mayor(num1, num2, num3)
'''
def multiplicador(cantidad):
    numeros = []
    for b in range(0, cantidad):
        numeros.append(int(input(">")))
    resultado = 1
    for c in range(0, cantidad):
        resultado = resultado * numeros[c]
    print("El resultado es> ")
    print(resultado)
cantidad = int(input("¿Cuántos números vas a multiplicar?> "))
multiplicador(cantidad)
'''
# def factorial(n):
#     if n == 0: return 1
#     else:
#         fac = 1
#         for i in range (1, n+1):
#             fac = fac*i
#     print(fac)
# factorial(int(input("Ingresa un numero a hacer factorial> ")))
def reversa(text):
    palabras = text.split(' ')
    palabra = ""
    for i in palabras[::-1]:
        palabra += i + " "
    print(palabra)
texto = input("Ingresa el String: ")
reversa(texto)