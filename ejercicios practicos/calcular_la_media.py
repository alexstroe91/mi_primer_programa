#definimos la lista como una lista vacia.

lista_numeros = []
numeros_lista = ""
#le decimos al usuario que para no meter más números en la lista, que diga YA

print("Para parar la lista escirbe 'YA' .")

#le pedimos al usuario que nos diga los numeros de la lista.

while not numeros_lista == "YA":
    numeros_lista = (input("Dime un número: ").upper())
    while numeros_lista.isdigit():
        lista_numeros.append(numeros_lista)
        numeros_lista = ""
        print("Número añadido.")

#calculamos la longitud de la lista.
longitud_lista = 0

#suma de todos los números

suma_numeros = 0

for numero in lista_numeros:
    suma_numeros = int(suma_numeros) + int(numero)

for numero in lista_numeros:
    longitud_lista += 1

promedio_longitud_lista = int(suma_numeros) / longitud_lista

print("La media de todos los números de la lista es {}".format(promedio_longitud_lista))

