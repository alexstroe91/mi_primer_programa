
frase_usuario = input("Introduce una frase:")

vocales = ["a", "e", "i", "o", "u"]

for letra in frase_usuario:
    if letra in vocales:
        print("Las vocales son '{}'".format(letra))