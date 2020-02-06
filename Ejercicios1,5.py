diccionario = {"Jorge":"07/12/2000", "Ana":"08/07/2000" , "Uriel":"02/07/1996"}
persona = input("Ingresa la persona que quieres buscar> ")
print(persona + " " + diccionario[persona])

#Se puede definir luego
diccionario["Bruno"] = "Lolis"
a = input("Ingresa la persona que quieres buscar> ")
print(diccionario[a])