#Pregunta al usuario una serie de 10 numeros y determina cual es el más pequeño de los 6

numeros_usuario = []
numero_del_usuario = ""

while len(numeros_usuario) < 6:
    while not numero_del_usuario.isdigit():
         numero_del_usuario = input("Dime un número: ")
     numeros_usuario.append(int(numero_del_usuario))
     numero_del_usuario = ""
    print("¡Número añadido!")

numero_pequeño = numeros_usuario[0]

for numero in numeros_usuario:
    if numero < numero_pequeño:
        numero_pequeño = numero

print("El número más pequeño es {}".format(numero_pequeño))