palabra = input("Ingresa una palabra:")
palabraL = list(palabra)

print("Es palindromo") if palabraL == list(reversed(palabraL)) else (print("No es palindromo"))
# if palabraL == list(reversed(palabraL())
#     print("Es palindromo") 
# else:
#     print("No es palindromo")