
frase_del_usuario = input("Introduce una frase: ")

vocales = ["a", "e", "i", "o", "u"]

numero_vocales = 0
numero_consonates = 0

for letra in frase_del_usuario:
    if letra in vocales:
        numero_vocales += 1
    else:
        numero_consonates += 1

print("Hay {} vocales en la frase".format(numero_vocales))
print("Hay {} consonantes en la frase".format(numero_consonates))