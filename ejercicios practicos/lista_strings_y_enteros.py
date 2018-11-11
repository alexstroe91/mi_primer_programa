
lista_mixta = [1, 2, "hola", 34, "hace frío"]

strings = []
enteros = []

for item in lista_mixta:
    if item is int :
        enteros.append(int(item))
    if item == str :
        enteros.append(str(item))



print ("Esta es la lista de las strings {}".format(strings))
print ("Esta es la lista de los enteros {}" .format(enteros))