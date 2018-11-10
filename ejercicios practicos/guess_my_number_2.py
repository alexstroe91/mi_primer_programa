
number_to_guess = int(input("Número a adivinar del 1 al 10. (Que tu amigo no lo vea): "))

guess_the_number = int(input("Adivina el número: "))

while guess_the_number != number_to_guess:
    if guess_the_number == number_to_guess:
        print("¡Has adivinado el número!")
    else:
        guess_the_number = (int(input("Adivina el número: ")))


print("¡Has adivinado el número!")