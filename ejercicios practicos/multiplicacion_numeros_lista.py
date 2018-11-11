
lista_numeros = [2, 2, 3, 4, 5, 6, 7, 8, 9]

multiplicacion = 1


for numero in lista_numeros:
    multiplicacion = int(numero) * int(multiplicacion)


print ("El resultado de la multiplicación de todos los números es {}".format (multiplicacion))
