numero1 = int(input("Ingresa un número> "))
numero2 = int(input("Ingresa otro número> "))


try:
    print(numero1/numero2)
except ArithmeticError as error:
    print(error)
    print("Esta operación no pudo ser realizada.")
    print("Error > " + str(error))