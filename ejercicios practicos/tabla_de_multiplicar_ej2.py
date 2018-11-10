
numero_usuario = int(input("Introduce el número que deseas multiplicar: "))

for multiplo in range(1, 11):
    resultado = (numero_usuario * multiplo )
    if (int(resultado%2 == 0)):
        print ("{} x {} = {} ".format(numero_usuario, multiplo, resultado))